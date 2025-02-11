from django.shortcuts import render

import argparse
import json
import os
import urllib
import urllib.request
import requests
import sys
from requests.auth import HTTPBasicAuth

from .models import Tags


def get_pretty_json(json_data):
    return json.dumps(json_data, indent=4, ensure_ascii=False)


def get_course_page(api_url, token):
    return json.loads(requests.get(api_url, headers={'Authorization': 'Bearer ' + token}).text)


def get_lessons(api_url, token, params):
    return json.loads(requests.get(api_url, headers={'Authorization': 'Bearer ' + token}, params=params).text)


def get_sections(api_url, token):
    return json.loads(requests.get(api_url, headers={'Authorization': 'Bearer ' + token}).text)


def get_all_weeks(stepik_resp):
    return stepik_resp['courses'][0]['sections']


def get_unit_list(section_list, token):
    resp = [json.loads(requests.get('https://stepik.org/api/sections/' + str(arr),
                                    headers={'Authorization': 'Bearer ' + token}).text)
            for arr in section_list]
    return [section['sections'][0]['units'] for section in resp]


def get_all_modules(stepik_course):
    return stepik_course['modules'][0]


def get_steps_list(units_list, week, token):
    data = [json.loads(requests.get('https://stepik.org/api/units/' + str(unit_id),
                                    headers={'Authorization': 'Bearer ' + token}).text)
            for unit_id in units_list[week - 1]]
    lesson_lists = [elem['units'][0]['lesson'] for elem in data]
    data = [json.loads(requests.get('https://stepik.org/api/lessons/' + str(lesson_id),
                                    headers={'Authorization': 'Bearer ' + token}).text)['lessons'][0]['steps']
            for lesson_id in lesson_lists]
    return [item for sublist in data for item in sublist]


def get_steps(api_url, token, lesson_id):
    steps_list = json.loads(requests.get('https://stepik.org/api/lessons/' + str(lesson_id), headers={'Authorization': 'Bearer ' + token}).text)['lessons'][0]['steps']

    steps_data = [get_pretty_json(json.loads(requests.get(api_url + str(step_id), headers={'Authorization': 'Bearer ' + token}).text))
                  for step_id in steps_list]
    return steps_data


def get_search_result(query, token):
    return json.loads(requests.get('https://stepik.org/api/search-results/',
                                   headers={'Authorization': 'Bearer ' + token}).text)


def get_tags(token):
    i = 1
    while True:
        params = {
            # 'tag': 'python',  # Искомый тег
            'page': i,  # Номер страницы результатов
            'page_size': 20  # Количество результатов на странице (может быть настроено)
        }

        tags = json.loads(requests.get('https://stepik.org/api/tags/',
                                       headers={'Authorization': 'Bearer ' + token}, params=params).text)
        for tag in tags['tags']:

            new_nag = Tags.objects.create(
                provider_tag_id=tag['id'],
                title=tag['title'],
                parent=tag['parent'],
                children=tag['children'],
                parents=tag['parents']
            )

            print(f'created {new_nag.id} {new_nag.title}')

        i += 1


def get_only_video_steps(step_list, token):
    resp_list = list()
    for s in step_list:
        resp = json.loads(requests.get('https://stepik.org/api/steps/' + str(s),
                                       headers={'Authorization': 'Bearer ' + token}).text)
        if resp['steps'][0]['block']['video']:
            resp_list.append(resp['steps'][0]['block'])
    print('Only video:', len(resp_list))
    return resp_list


def get_assignments(unit_id, token):
    data = json.loads(requests.get('https://stepik.org/api/units/' + str(unit_id), headers={'Authorization': 'Bearer ' + token}).text)

    assignment_lists = data['units'][0]['assignments']
    data = [json.loads(requests.get('https://stepik.org/api/assignments/' + str(assignment_id),
                                    headers={'Authorization': 'Bearer ' + token}).text)['assignments']
            for assignment_id in assignment_lists]
    return data


def parse_arguments():
    """
    Parse input arguments with help of argparse.
    """

    parser = argparse.ArgumentParser(
        description='Stepik downloader')

    # parser.add_argument('-c', '--client_id',
    #                     help='your client_id from https://stepik.org/oauth2/applications/',
    #                     required=True)

    # parser.add_argument('-s', '--client_secret',
    #                     help='your client_secret from https://stepik.org/oauth2/applications/',
    #                     required=True)

    parser.add_argument('-i', '--course_id',
                        help='course id',
                        required=True)

    parser.add_argument('-w', '--week_id',
                        help='week id starts from 1 (if not set then it will download the whole course)',
                        type=int,
                        default=None)

    # parser.add_argument('-q', '--quality',
    #                     help='quality of a video. Default is 720',
    #                     choices=['360', '720', '1080'],
    #                     default='720')

    # parser.add_argument('-o', '--output_dir',
    #                     help='output directory. Default is the current folder',
    #                     default='.')

    args = parser.parse_args()

    return args


def reporthook(blocknum, blocksize, totalsize):  # progressbar
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


def create_tags(request):
    # args = parse_arguments()

    """
    Example how to receive token from Stepik.org
    Token should also been add to every request header
    example: requests.get(api_url, headers={'Authorization': 'Bearer '+ token})
    """
    client_id = 'qGlHPrLQCd0235gNV1GK6cbTu2pXxhE4eEJIZ3xK'
    client_secret = 'AfdLSihXnMgmGYTfm9T1ym7qb4mvmQMfHp6mpCeiCJaxfbLEtfZPxZIEbzQiN9woUoFzZeKzW1Z96bUyrNIFsYclQw5zGUvo53BwoOB7Zmbl91W8Sk4Nkd1stNXanfA1'

    auth = HTTPBasicAuth(client_id, client_secret)
    resp = requests.post('https://stepik.org/oauth2/token/', data={'grant_type': 'client_credentials'}, auth=auth)
    token = json.loads(resp.text)['access_token']

    params = {
        'course': 210731
    }

    # courses_data = get_course_page('http://stepik.org/api/courses/', token)
    # print(get_pretty_json(courses_data))

    # for course in courses_data['courses']:
    #     print(course['title'], course['id'])

    # course_data = get_course_page('http://stepik.org/api/courses/' + '210731', token)
    # print(get_pretty_json(course_data))
    # units = get_lessons('http://stepik.org/api/units/', token, params)
    # print(get_pretty_json(units))
    # steps = get_steps('http://stepik.org/api/steps/', token, '1391178')
    # for step in steps:
    #     print(step)
    # print("--------------------------------------------------------")
    # print(course_data)

    # section_params = {
    #     'course': 210731
    # }

    # sections_data = get_sections('http://stepik.org/api/sections/' + '436368', token)
    # print(get_pretty_json(sections_data))

    # lessons_params = {
    #     'course': 210731
    # }
    # lessons_data = get_lessons('http://stepik.org/api/lessons/', token, lessons_params)
    # lesson_data = get_course_page('http://stepik.org/api/lessons/' + '1391178', token)
    # print(get_pretty_json(lesson_data))
    get_tags(token)
    # print(tags)

    # for tag in tags['tags']:
    #     print(tag['id'], tag['title'], tag['children'])

    # query = None
    # search_result = get_search_result(query, token)
    # print(search_result)
    # courses = search_result['search-results']
    # for course in courses:
    #     print(course['course'], course['course_title'])

    # weeks_num = get_all_weeks(course_data)
    #
    # all_units = get_unit_list(weeks_num, token)
    # # Loop through all week in a course and
    # # download all videos or
    # # download only for the week_id is passed as an argument.
    # for week in range(1, len(weeks_num)+1):
    #     # Skip if week_id is passed as an argument
    #     args_week_id = str(args.week_id)
    #     if args_week_id != "None":
    #         # week_id starts from 1 and week counts from 0!
    #         if week != int(args_week_id):
    #             continue
    #
        # all_steps = get_steps_list(all_units, week, token)
    #
    #     only_video_steps = get_only_video_steps(all_steps, token)
    #
    #     url_list_with_q = []
    #
    #     # Loop through videos and store the url link and the quality.
    #     for video_step in only_video_steps:
    #         video_link = None
    #         msg = None
    #
    #         # Check a video quality.
    #         for url in video_step['video']['urls']:
    #             if url['quality'] == args.quality:
    #                 video_link = url['url']
    #
    #         # If the is no required video quality then download
    #         # with the best available quality.
    #         if video_link is None:
    #             msg = "The requested quality = {} is not available!".format(args.quality)
    #
    #             video_link = video_step['video']['urls'][0]['url']
    #
    #         # Store link and quality.
    #         url_list_with_q.append({'url': video_link, 'msg': msg})
    #
    #     # Compose a folder name.
    #     folder_name = os.path.join(args.output_dir, args.course_id, 'week_' + str(week))
    #
    #     # Create a folder if needed.
    #     if not os.path.isdir(folder_name):
    #         try:
    #             # Create a directory for a particular week in the course.
    #             os.makedirs(folder_name)
    #         except PermissionError:
    #             print("Run the script from admin")
    #             exit(1)
    #         except FileExistsError:
    #             print("Please delete the folder " + folder_name)
    #             exit(1)
    #
    #     print('Folder_name ', folder_name)
    #
    #     for week, el in enumerate(url_list_with_q):
    #         # Print a message if something wrong.
    #         if el['msg']:
    #             print("{}".format(el['msg']))
    #
    #         filename = os.path.join(folder_name, 'Video_' + str(week) + '.mp4')
    #         if not os.path.isfile(filename):
    #             try:
    #                 print('Downloading file ', filename)
    #                 urllib.request.urlretrieve(el['url'], filename, reporthook)
    #                 print('Done')
    #             except urllib.error.ContentTooShortError:
    #                 os.remove(filename)
    #                 print('Error while downloading. File {} deleted:'.format(filename))
    #             except KeyboardInterrupt:
    #                 if os.path.isfile(filename):
    #                     os.remove(filename)
    #                 print('\nAborted')
    #                 exit(1)
    #         else:
    #             print('File {} already exist'.format(filename))
    #     print("All steps downloaded")


# if __name__ == "__main__":
#     main()
