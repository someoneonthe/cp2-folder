import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._comboBox4 = System.Windows.Forms.ComboBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 115)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(120, 60)
		self._button1.TabIndex = 3
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(140, 115)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(120, 60)
		self._label1.TabIndex = 4
		self._label1.Text = "label1"
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["The Master Thrasher",
			"The Dictator of Grind",
			"The Street King"]))
		self._comboBox1.Location = System.Drawing.Point(13, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(227, 37)
		self._comboBox1.TabIndex = 6
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["7.75 axle",
			"8 axle",
			"8.5 axle"]))
		self._comboBox2.Location = System.Drawing.Point(247, 13)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(116, 37)
		self._comboBox2.TabIndex = 7
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["51 mm",
			"55 mm",
			"58 mm",
			"61 mm"]))
		self._comboBox3.Location = System.Drawing.Point(370, 13)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(87, 37)
		self._comboBox3.TabIndex = 8
		# 
		# comboBox4
		# 
		self._comboBox4.FormattingEnabled = True
		self._comboBox4.Items.AddRange(System.Array[System.Object](
			["Grip tape",
			"Bearings",
			"Riser pads",
			"Nuts & bolts kit",
			"Assembly"]))
		self._comboBox4.Location = System.Drawing.Point(464, 13)
		self._comboBox4.Name = "comboBox4"
		self._comboBox4.Size = System.Drawing.Size(121, 37)
		self._comboBox4.TabIndex = 9
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(611, 261)
		self.Controls.Add(self._comboBox4)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Comic Sans MS", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog485Design"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		num = 0
		if self._comboBox1.Text == "The Master Thrasher":
			num += 60
		elif self._comboBox1.Text == "The Dictator of Grind":
			num += 45
		elif self._comboBox1.Text == "The Street King":
			num += 50
		if self._comboBox2.Text == "7.75 axle":
			num += 35
		elif self._comboBox2.Text == "8 axle":
			num += 40
		elif self._comboBox2.Text == "8.5 axle":
			num += 45
		if self._comboBox3.Text == "51 mm":
			num += 20
		if self._comboBox3.Text == "55 mm":
			num += 22
		if self._comboBox3.Text == "58 mm":
			num += 24
		if self._comboBox3.Text == "61 mm":
			num += 28
		if self._comboBox4.Text == "Grip tape":
			num += 10
		if self._comboBox4.Text == "Bearings":
			num += 30
		if self._comboBox4.Text == "Riser pads":
			num += 2
		if self._comboBox4.Text == "Nuts & bolts kit":
			num += 3
		if self._comboBox4.Text == "Assembly":
			num += 10
		self._label1.Text = str(num)