import os
def generate_event(event_name):
    newpath = 'athletics_events/'+ str(event_name) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return True