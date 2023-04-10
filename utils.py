from git import repo

import os
def generate_event(event_name):
    newpath = 'athletics_events/'+ str(event_name) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return True

def create_event_folder(event_name):
    g = Repo(self.rorepo.working_tree_dir)
    assert not repo.bare
    repo = g.get_repo("PyGithub/PyGithub")
    repo.create_file("example/test.txt", "test message", "content_of_file", branch="test")