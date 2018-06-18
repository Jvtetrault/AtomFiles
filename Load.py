# from clint.textui import progress
# import requests
#
#
# def pbar(path, url):
#     r = requests.get(url, stream=True)
#     if r.ok:
#         with open(path, 'wb') as f:
#             total_length = int(r.headers.get('content-length'))
#             centilength = total_length/100
#             for chunk in progress.bar(r.iter_content(chunk_size=centilength), expected_size=(centilength) + 1):
#                 if chunk:
#                     f.write(chunk)
#                     f.flush()
#     else:
#         print("Failed to download: " + str(path))
