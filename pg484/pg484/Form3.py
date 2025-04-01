
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form3(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 120)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(282, 32)
		self._label3.TabIndex = 11
		self._label3.Text = "Temperacher: -50C to  50C"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(11, 91)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(259, 29)
		self._label2.TabIndex = 10
		self._label2.Text = "Mass: 5.967 x 10^24"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(11, 63)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(259, 28)
		self._label1.TabIndex = 9
		self._label1.Text = "distance: 1 AU"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(123, 48)
		self._button1.TabIndex = 8
		self._button1.Text = "Back"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(141, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(111, 51)
		self._label4.TabIndex = 12
		self._label4.Text = "Earth Terrestrial"
		# 
		# Form3
		# 
		self.ClientSize = System.Drawing.Size(278, 165)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "Form3"
		self.Text = "Form3"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.myparent.Show()
		self.Close()