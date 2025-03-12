import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(259, 382)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(108, 55)
		self._button3.TabIndex = 7
		self._button3.Text = "quit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(147, 382)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 55)
		self._button2.TabIndex = 6
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(11, 382)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(130, 55)
		self._button1.TabIndex = 5
		self._button1.Text = "calc"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 25
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(356, 354)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(420, 447)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		num = 1
		while num <= 50:
			square = num * num
			root = round(math.sqrt(num))
			num += 1
			text = str(num) + "\t" + str(square) + "\t" + str(root)
			self._listBox1.Items.Add(text)