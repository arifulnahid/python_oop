class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

    def entry_show(self, id, movie, time):
        show = (id, movie, time)
        self.__seats_allowcate(id)
        self.__show_list.append(show)

    def __seats_allowcate(self, id):
        self.__seats[id] = []
        for row in range(self._rows):
            self.__seats[id].append(['free' * 1 for _ in range(self._cols)]) 

    def book_seats(self, id, seat):
        if seat[0] < 1 and seat[1] < 1:
            print("Invalid Seat")
        else: 
            try:
                if self.__seats[id][seat[0]-1][seat[1]-1] == 'free':
                    self.__seats[id][seat[0]-1][seat[1]-1] = 'booked'
            except IndexError:
                print("Invalid Seat")

    def view_show_list(self):
        print(self.__show_list)  

    def view_available_seats(self, id):
        print(self.__seats[id])             


class Star_Cinema(Hall):
    hall_list = []

    def __init__(self) -> None:
        pass

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)


hall1 = Hall(3, 2, 1)
cinema = Star_Cinema()
cinema.entry_hall(hall1)
cinema.hall_list[0].entry_show(1, 'hawa', '09:30 AM')
cinema.hall_list[0].book_seats(1,(1,2))
cinema.hall_list[0].view_show_list()
cinema.hall_list[0].view_available_seats(1)