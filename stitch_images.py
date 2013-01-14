from PIL import Image

def stitch_two_images(image1, image2, filename):
  '''Takes two .jpg pictures and a string filename and returns a stitched together picture'''
  im = Image.open(image1)
  im2 = Image.open(image2)
  width1,height1 = im.size
  width2,height2 = im2.size

  if height1 >= height2:
    heightfinal = im.size[1]
  else:
    heightfinal = im2.size[1]
  widthfinal = im.size[0] + im2.size[0]

  finalim = Image.new('RGB', ((widthfinal,heightfinal)))

  for w in range(width1):
    for h in range(height1):
      finalim.putpixel((w,h), im.getpixel((w,h)))

  for w in range(width2):
    for h in range(height2):
      if h-1<0:                                               #shift one pixel up
        finalim.putpixel((w+width1,h), im2.getpixel((w,h)))   #because input picture is different
      else:
        finalim.putpixel((w+width1,h-1), im2.getpixel((w,h)))

  finalim.save(filename + '.jpg', format = 'jpeg')

  return
