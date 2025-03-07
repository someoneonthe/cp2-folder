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
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 3
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(95, 115)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "label1"
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Normal",
			"Folding",
			"Roman"]))
		self._comboBox1.Location = System.Drawing.Point(12, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 5
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 inch",
			"27 inch",
			"32 inch",
			"40 inch"]))
		self._comboBox2.Location = System.Drawing.Point(140, 12)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(121, 21)
		self._comboBox2.TabIndex = 6
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural",
			"Blue",
			"Teal",
			"Red",
			"Green"]))
		self._comboBox3.Location = System.Drawing.Point(268, 12)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 7
		# 
		# comboBox4
		# 
		self._comboBox4.FormattingEnabled = True
		self._comboBox4.Location = System.Drawing.Point(122, 108)
		self._comboBox4.Name = "comboBox4"
		self._comboBox4.Size = System.Drawing.Size(121, 21)
		self._comboBox4.TabIndex = 8
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(407, 155)
		self.Controls.Add(self._comboBox4)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog485"
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		num = 50
		if self._comboBox1.Text == "Normal":
			num += 0
		elif self._comboBox1.Text == "Folding":
			num += 10
		elif self._comboBox1.Text == "Roman":
			num += 15
		if self._comboBox2.Text == "25 inch":
			num += 0
		elif self._comboBox2.Text == "27 inch":
			num += 2
		elif self._comboBox2.Text == "32 inch":
			num += 4
		elif self._comboBox2.Text == "40 inch":
			num += 6
		if self._comboBox3.Text == "Natural":
			num += 5
		else:
			num += 0
		self._label1.Text = str(num)