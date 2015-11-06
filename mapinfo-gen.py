from Tkinter import *
from Tkconstants import *
from ttk import *
import tkMessageBox
import tkFileDialog
import omg

class MapInfo():
    def __init__(self,mapid,blank=False):
        self.mapid = mapid
        
        if blank is True:
            self.title = ""
            self.author = ""
            self.music = ""
            self.sky = ""
            self.titlepatch = ""
            self.nextmap = ""
        else:
            self.title = "Rad Map"
            self.author = "Cool Mapper"
            self.music = "D_RUNNIN"
            self.sky = "SKY1"
            self.titlepatch = "CWILV00"
            if is_mapxx(mapid):
                self.nextmap = mapxx_gen(mapxx_decode(mapid)+1)
            else:
                self.nextmap = "E1M1"
            
        self.partime = 30
        
        
    def to_ZMAPINFO(self):
        output = ''
        output += 'map {id} "{title}" //{author}\n'.format(id=self.mapid, title=self.title, author=self.author)
        output += '{\n'
        if self.titlepatch != '': output += 'titlepatch = "{}"\n'.format(self.titlepatch)
        if self.sky != '': output += 'sky1 = "{}"\n'.format(self.sky)
        output += 'par = {}\n'.format(self.partime)
        if self.music != '': output += 'music = "{}"\n'.format(self.music)
        if self.nextmap != '': output += 'next = "{}"\n'.format(self.nextmap)
        if self.mapid == "MAP07":
            output += 'map07special\n'
        if self.mapid == "E1M8":
            output += 'baronspecial\n'
        if self.mapid == "MAP15":
            output += 'secretnext = "MAP30"\n'
        if self.mapid == "MAP30":
            output += 'secretnext = "MAP31"\n'
        output += '}\n'
        return output
        
    def to_EMAPINFO(self):
        output = ''
        output += '[{}]\n'.format(self.mapid)
        output += 'levelname = {}\n'.format(self.title)
        if self.author != '': output += 'creator = {}\n'.format(self.author)
        if self.sky != '': output += 'skyname = {}\n'.format(self.sky)
        if self.titlepatch != '': output += 'levelpic = {}\n'.format(self.titlepatch)
        if self.music != '': output += 'music = {}\n'.format(self.music)
        if self.nextmap != '': output += 'nextlevel = {}\n'.format(self.nextmap)
        if self.mapid == "MAP15":
            output += 'nextsecret = MAP30\n'
        if self.mapid == "MAP30":
            output += 'nextsecret = MAP31\n'
        output += 'partime = {}\n'.format(self.partime)
        return output
        
    def to_DEHACKED_STRING(self):
        output = ''
        output += 'HUSTR_{} = {}: {}\n'.format(self.mapid[3:],self.mapid,self.title)
        return output
        
    def to_DEHACKED_PAR(self):
        output = ''
        output += 'PAR {} {}\n'.format(mapxx_decode(self.mapid),self.partime)
        return output
        
def mapxx_gen(id):
    if id < 10:
        xx = "0"+str(id)
    else:
        xx = str(id)
    return "MAP"+xx
    
def mapxx_decode(str):
    return int(str[3:])
    
def is_mapxx(str):
    return str.find("MAP") == 0

class MapInfoEditor(Frame):
    def __init__(self,parent,main,mapinfo=None):
        Frame.__init__(self, parent)
        self.main = main
        if mapinfo is None:
            self.mapinfo = MapInfo("MAP",blank=True)
        else:
            self.mapinfo = mapinfo
        self.build_view()
    
    def build_view(self):
        self.text_maplump = Entry(self, wrap=None, width=30)
        self.text_maplump.insert(END, self.mapinfo.mapid)
        self.text_maplump.grid(row=0, column=1)
        self.label_maplump = Label(self, text="Map Lump")
        self.label_maplump.grid(row=0,column=0,sticky=E)
    
        self.text_mapname = Entry(self, wrap=None, width=30)
        self.text_mapname.insert(END, self.mapinfo.title)
        self.text_mapname.grid(row=1, column=1)
        self.label_mapname = Label(self, text="Mapname")
        self.label_mapname.grid(row=1,column=0,sticky=E)
        
        self.text_author = Entry(self, wrap=None, width=30)
        self.text_author.insert(END, self.mapinfo.author)
        self.text_author.grid(row=2, column=1)
        self.label_author = Label(self, text="Author")
        self.label_author.grid(row=2,column=0,sticky=E)
        
        self.text_musiclump = Entry(self, wrap=None, width=30)
        self.text_musiclump.insert(END, self.mapinfo.music)
        self.text_musiclump.grid(row=3, column=1)
        self.label_musiclump = Label(self, text="Music")
        self.label_musiclump.grid(row=3,column=0,sticky=E)
        
        self.text_skylump = Entry(self, wrap=None, width=30)
        self.text_skylump.insert(END, self.mapinfo.sky)
        self.text_skylump.grid(row=4, column=1)
        self.label_skylump = Label(self, text="Sky")
        self.label_skylump.grid(row=4,column=0,sticky=E)
        
        self.text_titlepatch = Entry(self, wrap=None, width=30)
        self.text_titlepatch.insert(END, self.mapinfo.titlepatch)
        self.text_titlepatch.grid(row=5, column=1)
        self.label_titlepatch = Label(self, text="Title patch")
        self.label_titlepatch.grid(row=5,column=0,sticky=E)
        
        self.text_nextmap = Entry(self, wrap=None, width=30)
        self.text_nextmap.insert(END, self.mapinfo.nextmap)
        self.text_nextmap.grid(row=6, column=1)
        self.label_nextmap = Label(self, text="Next map")
        self.label_nextmap.grid(row=6,column=0,sticky=E)
        
        self.text_partime = Entry(self, wrap=None, width=30)
        self.text_partime.insert(END, self.mapinfo.partime)
        self.text_partime.grid(row=7, column=1)
        self.label_partime = Label(self, text="Par time")
        self.label_partime.grid(row=7,column=0,sticky=E)
        
        self.button_save = Button(self, text="Add", command=self.full_save)
        self.button_save.grid(row=8,column=0, columnspan=2)
        
    def full_save(self):
        self.save()
        
        self.main.save_map(self.mapinfo.mapid,self.mapinfo)
        tkMessageBox.showinfo("done","map saved")
        self.main.build_maplist()
        
        
    def save(self):
    
        self.mapinfo.mapid = self.text_maplump.get()
        self.mapinfo.title = self.text_mapname.get()
        self.mapinfo.author = self.text_author.get()
        self.mapinfo.music = self.text_musiclump.get()
        self.mapinfo.sky = self.text_skylump.get()
        self.mapinfo.titlepatch = self.text_titlepatch.get()
        self.mapinfo.nextmap = self.text_nextmap.get()
        self.mapinfo.partime = int(self.text_partime.get())
        
        
class MainWindow(Tk):
    def __init__(self,parent):
        Tk.__init__(self, parent)
        self.mapinfolist = MapInfoList()
        self.geometry("360x480")
        self.title("mapinfo-gen")
        self.create_frame()
        self.maplist = None
        self.editor = None
        self.build_view()
        
        
    def create_frame(self):
        self.frame = Frame(self, width=360, height=480)
        self.frame.grid(sticky="NSWE")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
    def build_view(self):
        self.build_maplist()
        
        self.button_newmap = Button(self.frame, text="New map", command=self.new_map)
        self.button_newmap.grid(row=1,column=0,sticky="s")
        
        self.button_delmap = Button(self.frame, text="Delete map", command=self.del_map)
        self.button_delmap.grid(row=2,column=0,sticky="s")
        
        self.button_load = Button(self.frame, text="Load WAD", command=self.load)
        self.button_load.grid(row=3,column=0,sticky="s")
        
        self.button_save = Button(self.frame, text="Save WAD", command=self.save)
        self.button_save.grid(row=4,column=0,sticky="s")
        
        self.build_mapinfoeditor()
        
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        
    def build_mapinfoeditor(self,data=None):
        if self.editor is not None:
            self.editor.save()
            self.editor.destroy()
        
        if data is None:
            self.editor = MapInfoEditor(self.frame,self)
        else:
            self.editor = MapInfoEditor(self.frame,self,mapinfo=data)
            
        self.editor.grid(row=0, column=1, rowspan=4, sticky="nesw")
        
    def build_maplist(self):
        if self.maplist is not None:
            self.maplist.destroy()
        
        self.maplist = Treeview(self.frame)
        self.maplist.heading("#0", text = "maps")
        self.maplist.column("#0",minwidth=0,width=100)
        self.maplist.grid(row=0,column=0,sticky="nws")
        
        for m in self.mapinfolist.maps:
            self.maplist.insert('', len(self.maplist.get_children('')), text=m.mapid)
            
        def on_select(event):
            index = int(self.maplist.selection()[0][1:])-1
            self.build_mapinfoeditor(self.mapinfolist.maps[index])
                
        self.maplist.bind("<<TreeviewSelect>>", on_select)
        
    def del_map(self):
        index = int(self.maplist.selection()[0][1:])-1
        self.mapinfolist.maps.remove(self.mapinfolist.maps[index])
        self.build_maplist()
        
    def new_map(self):
        self.build_mapinfoeditor()
        self.build_maplist()
        
    def load(self):
        f = tkFileDialog.askopenfilename(defaultextension=".wad")
        if f is None:
            return
        wad = omg.WAD(str(f))
        self.mapinfolist.read_wad(wad)
        tkMessageBox.showinfo("load","loaded successfully")
        self.build_maplist()
        
    def save_map(self,mapid,data):
        self.mapinfolist.save_map(mapid,data)
        
    def save(self):
        f = tkFileDialog.asksaveasfilename(defaultextension=".wad")
        if f is None:
            return
        wad = self.mapinfolist.to_wad()
        wad.to_file(f)
        tkMessageBox.showinfo("done","wad saved correctly")
        
        
class MapInfoList():
    def __init__(self):
        self.maps = []
        
    def to_wad(self):
        output = omg.WAD()
        output.data["ZMAPINFO"] = omg.Lump(self.to_ZMAPINFO())
        output.data["EMAPINFO"] = omg.Lump(self.to_EMAPINFO())
        output.data["DEHACKED"] = omg.Lump(self.to_DEHACKED())
        return output
        
    def save_map(self,mapid,data):
        if data not in self.maps:
            self.maps.append(data)
        
    def read_wad(self,wad):
        self.maps = []
        for m in wad.maps:
            self.maps.append(MapInfo(m,blank=True))
        
    def to_ZMAPINFO(self):
        output = ''
        for m in self.maps:
            output += m.to_ZMAPINFO()
        return output
    
    def to_EMAPINFO(self):
        output = ''
        for m in self.maps:
            output += m.to_EMAPINFO()
        return output
    
    def to_DEHACKED(self):
        output = ''
        output += '[STRINGS]\n'
        for m in self.maps:
            output += m.to_DEHACKED_STRING()
        output += '[PARS]\n'
        for m in self.maps:
            output += m.to_DEHACKED_PAR()
        return output

if __name__ == "__main__":
    app = MainWindow(None)
    # MapInfoEditor(app).grid()
    
    app.mainloop()