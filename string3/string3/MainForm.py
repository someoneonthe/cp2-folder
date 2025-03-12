import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(182, 31)
		self._textBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 104)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 47)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(148, 104)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 47)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(92, 166)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 47)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(15, 54)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(235, 47)
		self._label1.TabIndex = 4
		self._label1.Text = "label1"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(262, 225)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "string3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		word = self._textBox1.Text
		num = int[word]
		let = 0
		dup = 1
		while dup < len(word):
			if word[int(let)] != word[int(dup)]:
				dup += 1
			else:
				let += 1
				dup = 0
		
			