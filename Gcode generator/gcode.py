#! /usr/bin/env python
import gtk
gflag = True 
file = open("Gcode.txt", "w+r")
class gcode1:
    def on_window1_destroy(self, object, data=None):
        print("Quit window")
        file.close()
        gtk.main_quit()

    def __init__(self):
        self.gladefile = "gcode.glade"
        self.builder = gtk.Builder()
        self.settings = gtk.settings_get_default()
        self.settings.set_property("gtk-theme-name", "Adwaita-dark")
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.window.show()
        self.notebook = self.builder.get_object("notebook1")
        self.notebook.connect("switch_page", self.callback2)
        
    
    def callback2(self, notebook, tab, index):
        
        if index == 0:
            gflag == True

            print("Automatic gcode generator")

        elif index == 1:
            gflag == False
            print("CSV Upload")

    def degree_select(self , widget ):
        self.degree = 90
        if widget.get_active():
           self.degree = (gtk.Buildable.get_name(widget))
           print("\n " + self.degree)

    
    def on_generate_clicked(self, widget, dat=None):
        print("generation button clicked")
        self.xoff1 = 0
        self.yoff1 = 0
        self.ns1 = float(self.builder.get_object("ns").get_text())
        self.ds1 = int(self.builder.get_object("ds").get_text())
        self.xoff1 = float(self.builder.get_object("xoff").get_text())
        self.yoff1 = float(self.builder.get_object("yoff").get_text())
        print(gflag)
        if gflag == True:
            self.pitchx = float(self.builder.get_object("pitchx").get_text())
            self.pitchy = float(self.builder.get_object("pitchy").get_text())
            self.nx1 = int(self.builder.get_object("nx").get_text())
            self.ny1 = int(self.builder.get_object("ny").get_text())
            file.write("\n G90 G21 \n G28")
            if self.degree == "90":
                print("case entered ")
                #file.write("\n G90 G21 \n G28")

                file.write("\n G00 X" + str(self.xoff1-self.pitchx
                                                 ) + " Y" + str(self.yoff1-self.pitchy))
                file.write("\n G91  ")
                file.write("\n M98 P2000 L" + str(self.ny1))
                file.write("\n 04000 ")
                file.write("\n G01 Y" + str(self.pitchy) + "F5000")
                file.write("\n M98 P4000 L" + str(self.nx1))
                file.write("\n O4000")
                file.write("\n G01 X" + str(self.pitchx) + "F5000")
                file.write("\n M98 P8000 L" +str(self.ns1))                
                file.write("\n 08000")
                file.write("\n M7 \n G04 P3 \M9")
                file.write("\n G01 Y"+ str(self.ds1) + "F5000")
                file.write("\n M99")
                file.write("\n G01 -Y"+str( float(self.ns1*self.ds1)))
                file.write("\n M99")
                file.write("\n M99")
                file.write("\n G28 \n M30 ")
                file.write("\n ")
                file.close()
            elif self.degree == 45:
                print(" Honey Comb")
        else:
            print("hohoho")


if __name__ == "__main__":
    main = gcode1()
    gtk.main()
