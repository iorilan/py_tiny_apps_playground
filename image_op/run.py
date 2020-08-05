import helper
import os 


    

def test_sample_lines():
    helper.draw_sample_lines(os.path.join('sample_data','sample_lines.png'))
    helper.show(os.path.join('sample_data','sample_lines.png'))

def test_sample_rect():
    helper.draw_sample_rect(os.path.join('sample_data','sample_rect.png'))
    helper.show(os.path.join('sample_data','sample_rect.png'))

def test_sample_circle():
    helper.draw_sample_circle(os.path.join('sample_data','sample_circle.png'))
    helper.show(os.path.join('sample_data','sample_circle.png'))


"""
    saving format have to be png
"""
def test_create_with_color():
    helper.create_with_color(path=os.path.join('sample_data','create_with_color.png'))
    helper.show(os.path.join('sample_data','create_with_color.png'))

def test_create_transparent():
    helper.create_transparent(path=os.path.join('sample_data','create_trans.png'))
    helper.show(os.path.join('sample_data','create_trans.png'))

def test_image_crop():
    helper.crop(os.path.join('sample_data','sample_circle.png'),(100,20,200,100),os.path.join('sample_data','cropped.png'))
    helper.show(os.path.join('sample_data','cropped.png'))

def test_merge():
    img1 = os.path.join('sample_data','sample_lines.png')
    img2 = os.path.join('sample_data','cropped.png')
    img3 = os.path.join('sample_data','merged.png')
    helper.merge(img2,img1,img3,(150,150))
    helper.show(img3)

def test_resize():
    img1 = os.path.join('sample_data','merged.png')
    img2 = os.path.join('sample_data','resized.png')
    #helper.resize(img1,0.5,img2)
    helper.resize(img1,2,img2)
    helper.show(img2)

def test_rotate():
    img1 = os.path.join('sample_data','resized.png')

    # img2 = os.path.join('sample_data','rotated.png')
    # helper.rotate(img1,60,img2)
    # helper.show(img2)

    # img3 = os.path.join('sample_data','horizental_flip.png')
    # helper.flip_horizontal(img1,img3)
    # helper.show(img3)

    img4 = os.path.join('sample_data','vertical_flip.png')
    helper.flip_vertical(img1,img4)
    helper.show(img4)

def test_fill_on_img():
    img1 = os.path.join('sample_data','sample_lines.png')
    img2 = os.path.join('sample_data','sample_lines_filled.png')
    helper.fill_color(img1, img2, left_top=(50,100))
    helper.show(img2)

def test_blur_gray():
    img1 = os.path.join('sample_data','sample_lines_filled.png')

    # img2 = os.path.join('sample_data','blur.png')
    # helper.blur(img1,img2)
    # helper.show(img2)

    img3 = os.path.join('sample_data','gray.png')
    helper.gray_scale(img1,img3)
    helper.show(img3)

def test_watermark():
    img1 = os.path.join('sample_data','rotated.png')
    img2 = os.path.join('sample_data','watermark.png')
    helper.watermark(img1,img2,'by iorilan',(700,100))
    helper.show(img2)

def test_download():
    url = 'https://www.google.com/logos/doodles/2020/wear-a-mask-save-lives-copy-6753651837108810-s.png'
    img1 = os.path.join('sample_data','download.png')
    helper.download(url, img1)
    helper.show(img1)

if __name__ == "__main__":
    test_sample_lines()
    #test_sample_rect()
    #test_sample_circle()

    #test_image_crop()
    
    #test_merge()
    #test_resize()
    #test_rotate()
    #test_fill_on_img()
    #test_blur_gray()
    #test_watermark()
    #test_download()