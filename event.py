class Event:
    def __init__(self, start_time, end_time, event_text, day_id):
        if start_time <= end_time:
            self.start_time = start_time
            self.end_time = end_time
            self.event_text = event_text
            self.day_id = day_id
            try:
                self.day_id = int(day_id)
            except ValueError:
                print('Invalid value for day_id; must be a positive integer')
        else:
            raise ValueError('End point is lesser than start point')

if __name__ == '__main__':
    c = Event((12, 00), (13, 30), 'sample text', 0)
    #d = Event((13, 30), (12, 00), 'sample text', 0)
    print(c.event_text)
