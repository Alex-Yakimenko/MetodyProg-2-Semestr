

class List:

    ostov_liver = []

    class node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node




    class duga:
        e1 = None
        e2 = None
        ves = None
        nap = False
        next_duga = None

        def __init__(self, e1, e2, ves = None, nap = False, next_duga = None):
            self.e1 = e1
            self.e2 = e2
            self.ves = ves
            self.nap = nap
            self.next_duga = next_duga

    graff_size = 0









    head = node
    heaDug = duga

    #Работа с дугами

    def gendg(self, e1, e2, ves = None, nap = False):
        if self.heaDug.e1 == None:
            self.heaDug = self.duga(e1, e2, ves, nap)
        else:
            current = self.heaDug

            while current.next_duga != None:
                current = current.next_duga

            current.next_duga = self.duga(e1, e2, ves, nap)

    def dgout(self, el):
        current = self.heaDug       
        
        while current.next_duga != None:
            if current.nap == False:
                if current.e1 == el:
                    print("|**|", current.e1 , "--", current.e2, " ", current.ves)
                elif current.e2 == el:
                    print("|**|", current.e2, "--", current.e1, " ", current.ves)
            else:
                if current.e1 == el:
                    print("|**|", current.e1 , "-->", current.e2, " ", current.ves)
            current = current.next_duga

        if current.nap == False:
            if current.e1 == el:
                print("|**|", current.e1 , "--", current.e2, " ", current.ves)
            elif current.e2 == el:
                print("|**|", current.e2, "--", current.e1, " ", current.ves)
        else:
            if current.e1 == el:
                print("|**|", current.e1 , "-->", current.e2, " ", current.ves)

    def deld(self, element1, element2):
        current = self.heaDug
        prev_node = current

        if (current.e1 == element1) and (current.e2 == element2):
            self.heaDug = current.next_duga
            del current
        else:
            while current.next_duga != Neno:
                if (current.e1 == element1) and (current.e2 == element2):
                    prev_node.next_duga = current.next_duga
                    del current
                prev_node = current
                current = current.next_duga

    #Работа с точками.
    
    def gent(self, element):
        if self.head.element == None:
            self.head = self.node(element)
            self.graff_size = self.graff_size + 1
        else:
            current = self.head

            while current.next_node != None:
                current = current.next_node

            current.next_node = self.node(element)
            self.graff_size = self.graff_size + 1

    def delt(self, element):
        current = self.head

        if current.element == element:
            self.head = current.next_node
            del current
            self.graff_size = self.graff_size - 1
        else:
            prev_node = current

            while current.element != element:
                prev_node = current
                current = current.next_node

            prev_node.next_node = current.next_node
            del current
            self.graff_size = self.graff_size - 1

    def out(self):
        current = self.head

        while current.next_node != None:
            print(current.element)
            self.dgout(current.element)
            current = current.next_node
        print(current.element)
        self.dgout(current.element)

    #Вывод данных

    def ask_for_element(self, element):
        current = self.head

        while current.element != element:
            current = current.next_node

        return current.element

    def ask_about_element(self, element):
        current = self.heaDug
        arr = []

        while current.next_duga != None:

            if current.e1 == element:
                arr.append(self.ask_for_element(current.e2))
            elif current.e2 == element:
                arr.append(self.ask_for_element(current.e1))
            current = current.next_duga

        if current.e1 == element:
            arr.append(self.ask_for_element(current.e2))
        elif current.e2 == element:
            arr.append(self.ask_for_element(current.e1))

        return arr

    def chek_liver(self, element):
        i = 0
        while i < len(self.ostov_liver):
            #print(self.ostov_liver[i])
            if self.ostov_liver[i][0] == element:
                return False
            i = i + 1
        return True

    def serch_for_lvl(self, lvl):
        i = 0
        while i < len(self.ostov_liver):
            if self.ostov_liver[i][2] == False:
                if lvl > self.ostov_liver[i][1]:
                    return True
            i = i + 1
        return False

    def do_for_true(self, element):
        i = 0
        while i < len(self.ostov_liver):
            if self.ostov_liver[i][0] == element:
                self.ostov_liver[i][2] = True
            i = i + 1
    
    def create_ostov(self, element, lvl = 0):
        #self.do_for_true(element)

        out = []
        current = self.head
        while current.element != element:
            current = current.next_node
        
        arr = self.ask_about_element(current.element)
        if self.chek_liver(element):
            self.ostov_liver.append([element, lvl, True])
        if self.serch_for_lvl(lvl):
            return None
        print(element)
        #print(self.ostov_liver)

        i = 0
        while i < len(arr):
            if self.chek_liver(arr[i]):
                out.append(arr[i])
                self.ostov_liver.append([arr[i], lvl + 1, False])
                
            i = i + 1
        print(out)
        
        i = 0
        while i < len(self.ostov_liver):
            self.create_ostov(self.ostov_liver[i][0], lvl + 1)
            i = i + 1

    def follow_the_way(self, element, arr):
        i = 0
        while i < len(arr):
            if arr[i][0] == element:
                return False
            i = i + 1
        return True

    def the_way(self, start_element, end_element):
        ways = []
        arr = []
        to_add = []

        to_add.append(start_element)
        to_add.append(str(start_element))

        ways.append(to_add)

        i = 0
        while i < len(ways):
            arr = self.ask_about_element(ways[i][0])
            j = 0
            while j < len(arr):
                if self.follow_the_way(arr[j], ways):
                    to_add = []
                    to_add.append(arr[j])
                    to_add.append(str(ways[i][1])+str(arr[j]))
                    ways.append(to_add)
                    if arr[j] == end_element:
                        return ways[-1][1]
                j = j + 1
            
            i = i + 1
        print(ways)

    def chek_filde(self, arr_of, element):
        i = 0
        while i < len(arr_of):
            if arr_of[i] == element:
                return False
            i = i + 1
        return True


    def build_filde(self, element):
        filde = []
        arr = []

        filde.append(element)

        i = 0
        while i < len(filde):
            arr = self.ask_about_element(filde[i])
            j = 0
            while j < len(arr):
                if self.chek_filde(filde, arr[j]):
                    filde.append(arr[j])
                j = j + 1
            i = i + 1

        return filde

    def arr_filde_chek(self, arr, element):
        i = 0
        while i < len(arr):
            j = 0
            while j < len(arr[i]):
                if element == arr[i][j]:
                    return False
                j = j + 1
            i = i + 1
        return True

    def connect_chek(self):
        current = self.head
        
        arr_of_filde = [] #список полей

        filde = self.build_filde(current.element)
        arr_of_filde.append(filde)

        while current.next_node != None:
            if self.arr_filde_chek(arr_of_filde, current.element):
                filde = self.build_filde(current.element)
                arr_of_filde.append(filde)

            current = current.next_node

        if self.arr_filde_chek(arr_of_filde, current.element):
            print('!')
            filde = self.build_filde(current.element)
            arr_of_filde.append(filde)

        #print(arr_of_filde)
        return arr_of_filde

    def to_filde_chek(self, element):
        arr_of_filde = self.connect_chek()
        i = 0
        while i < len(arr_of_filde):
            j = 0
            while j < len(arr_of_filde[i]):
                if element == arr_of_filde[i][j]:
                    return (arr_of_filde[i])
                j = j + 1
            i = i + 1
                
    def chek_for_own_fild(self, element1, element2):
        arr_of_filde = self.to_filde_chek(element1)
        i = 0
        while i < len(arr_of_filde):
            #print(element2, arr_of_filde[i])
            if element2 == arr_of_filde[i]:
                #print('!')
                return True
            i = i + 1

        return False

def gen_ostov(sas, element):
    sas.create_ostov(element)
    sas.ostov_liver = []
def own_fild(sas, element1, element2):
    return sas.chek_for_own_fild(element1, element2)
def short_way(sas, start, stop):
    return(sas.the_way(start, stop))
def filde_show(sas):
    return sas.connect_chek()
def whiche_fild(sas, element):
    return sas.to_filde_chek(element)
def graf_gen():
    return List()
def add_toch(sas, num):
    sas.gent(num)
def add_dg(sas, e1, e2, mas = None):
    sas.gendg(e1, e2, mas)
def add_ndg(sas, e1, e2, mas = None):
    sas.gendg(e1, e2, mas, True)
def al_out(sas):
    sas.out()
def del_toch(sas, num):
    sas.delt(num)
def del_dug(sas, e1, e2):
    sas.deld(e1, e2)
def Ask_for_next(sas, element):
    return sas.askForDuga(element)