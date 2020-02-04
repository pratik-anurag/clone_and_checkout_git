import git
import os
import re
from git import Repo
clone_path = "path to local folder"
remote_url = "https://path_to_bitbucket@bitbucket.org/"
def run():
    f_obj = open(os.path.join(os.path.dirname(__file__),  'fixed_ops_repos.txt'))
    regex = re.compile('^.*\d.*$')
    for line in f_obj.readlines():
        line = line.strip().replace(' ', '-')
        if line!="" and not regex.match(line):
            print(line)
            repo_name = line.lower()
            print(clone_path + repo_name)
            if not os.path.exists(clone_path + repo_name):
                git.Git(clone_path).clone(remote_url + repo_name + '.git')
            else:    
                r = Repo(clone_path+repo_name)
                repo_heads = r.heads
                repo_heads_names = [h.name for h in repo_heads]
                if 'branch' in repo_heads_names:
                    repo_heads['branch'].checkout()
                else:
                    print(repo_heads_names)
                    repo_heads[repo_heads_names[0]].checkout()
if __name__ == "__main__":
    run()
