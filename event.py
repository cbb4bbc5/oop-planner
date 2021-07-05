class Event:
    def __init__(self, event_text, day_id, start_time=None, end_time=None):
        if start_time == None and end_time == None:
            self.create_from_text(event_text, day_id)
            return
        if start_time <= end_time:
            self.start_time = start_time
            self.end_time = end_time
            self.event_text = event_text
            self.day_id = day_id
            try:
                self.day_id = int(day_id)
            except ValueError:
                raise ValueError('Invalid value for day_id; must be a positive integer')
        else:
            raise ValueError('End point is lesser than start point')
    
    def get_id(self):
        return self.day_id
    
    def create_from_text(self, text, day_id):
        # the only accepted format
        # start end
        # HH:MM-HH:MM-event_text(can be with spaces)
        # provide only start end and text
        data = text.split('-')
        self.start_time = self.__get_hour__(data[0])
        self.end_time = self.__get_hour__(data[1])
        self.event_text = data[2]
        self.day_id = int(day_id)
    
    # TODO:
    # make this "public" 
    def __get_hour__(self, hour):
        h_tmp = tuple(int(h) for h in hour.split(':'))
        return h_tmp
    
    def get_start(self):
        return self.start_time

    def get_end(self):
        return self.end_time
    
    def get_text(self):
        return self.event_text

if __name__ == '__main__':
    # sample input
    c = Event('sample text', '0', (12, 00), (13, 30))
    d = Event('14:15-16:29-test text', '1')
    print(c.event_text)
    print(d.event_text, d.start_time)
