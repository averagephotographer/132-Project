from Tkinter import *
from tkFont import Font

class WaveformVis(Canvas):
  # dimensions of Pi screen
  WIDTH = 800
  HEIGHT = 450
  MID_Y = HEIGHT / 2

  def __init__(self, bgColor = 'white'):
    window = Tk()
    window.geometry("{}x{}".format(WaveformVis.WIDTH, WaveformVis.HEIGHT))
    window.title("Paper Piano Waveform Visualizer")
    Canvas.__init__(self, window, bg=bgColor)
    self.pack(fill=BOTH, expand=1)
    self.window = window

  def visSamples(self, samples, waveformName, color = 'blue', axisAndTitleColor = 'black'):
    # so we don't go off screen
    AMP_SCALE_BACK = 150
    
    x = 0
    rectWidth = 1
    
    # repeat for a certain number of periods (so we can clearly see the pattern)
    for p in range(20):
      # go through each sample
      for sample in samples:
        scaledSample = sample / AMP_SCALE_BACK
        if scaledSample >= 0:
          top = WaveformVis.MID_Y - scaledSample
          bottom = WaveformVis.MID_Y
        else:
          top = WaveformVis.MID_Y
          bottom = WaveformVis.MID_Y - scaledSample
        
        # plot the sample
        self.create_rectangle(x, int(top), x+rectWidth, int(bottom), fill=color, outline=color)
        x += rectWidth
        
    # plot the axes
    self.create_rectangle(0, WaveformVis.MID_Y-1, WaveformVis.WIDTH, WaveformVis.MID_Y+1, fill=axisAndTitleColor, outline=axisAndTitleColor)
    self.create_rectangle(2, 0, 2, WaveformVis.HEIGHT, fill=axisAndTitleColor, outline=axisAndTitleColor)
    
    # show the waveform name
    font = Font(family='Times New Roman', size=18)
    self.create_text(WaveformVis.WIDTH / 2, 30, font=font, text=waveformName.title(), fill=axisAndTitleColor)

    # render it
    self.window.mainloop()

# Usage for Paper Piano Assignment:
# -----------------------------------------------------------------
# add the following line of code at the top of your file:
#   from waveform_vis import WaveformVis
#
# now in your build_samples function, after generating your samples,
# add the following lines of code
#    vis = WaveformVis()
#    vis.visSamples(samples, waveform_name)
