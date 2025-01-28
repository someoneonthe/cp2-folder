import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(10, 146)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 36)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(116, 146)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 36)
		self._button2.TabIndex = 1
		self._button2.Text = "Erase"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(222, 146)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 36)
		self._button3.TabIndex = 2
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightGray
		self._label1.Location = System.Drawing.Point(11, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(310, 126)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(311, 138)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(10, 10)
		self._button4.TabIndex = 4
		self._button4.Text = "button4"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(333, 201)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "about me"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "I'm Nicholas and I like games. Coding is just a hobby I used to do in gamemaker studio."

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button4Click(self, sender, e):
		self._label1.Text = "Why did you clck this?"