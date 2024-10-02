from github import Github, Auth
import json
import os
from MarkdownGuide import main

def upload(release, filepath, name = None):
    if os.path.exists(filepath):
        if name == None:
            name = os.path.basename(filepath)
        release.upload_asset(
            path = filepath,
            label = name,
            content_type = "application/octet-stream"
        )
if __name__ == '__main__':
    g = Github(auth = Auth.Token(os.environ.get('GITHUB_TOKEN')))
    repo = g.get_repo("364hao/Test")
    resDir = os.path.abspath('Phigros_Resource')
    with open(os.path.join(resDir, 'manifest.json'), 'r', encoding = 'utf-8') as f:
        version = json.load(f)['version_name']
    r = repo.create_git_release(
        tag = 'v' + version,
        name = f'Version {version} full assests',
        message = "From Apkpure, Github Action bot Generate"
    )
    upload(r, os.path.join(resDir, 'icon.png'))
    upload(r, os.path.join(resDir, 'difficulty.tsv'))
    upload(r, os.path.join(resDir, 'collection.tsv'))
    upload(r, os.path.join(resDir, 'avatar.txt'))
    upload(r, os.path.join(resDir, 'illustration.txt'))
    upload(r, os.path.join(resDir, 'info.tsv'))
    upload(r, os.path.join(resDir, 'music-info.json'))
    upload(r, os.path.join(resDir, 'tips.txt'))
    upload(r, os.path.join(resDir, 'single.txt'))
    main(r, upload)