import camogen



def setting(opt):
    colors = ['#264722', '#023600', '#181F16']

    color_parameters = {'width': opt.width, 'height': opt.height, 'polygon_size': opt.polygon_size, 'color_bleed': opt.color_bleed,
                  'colors': opt.colors, 'spots': {'amount': opt.num_spot, 'radius': opt.radius, 'sampling_variation': opt.spot_var}, 'pixelize': {'percentage': opt.pixel_scale, 'sampling_variation': opt.pixel_var, 'density': opt.density}}

    return color_parameters
def run_generator(folder_n, num_image, opt):

    i = 1
    color_param = setting(opt)
    while i <= num_image:
        image = camogen.generate(color_param)
        image.save("./background{0}/background_blots_{1}.jpg".format(folder_n,i))
        print("./background//background_blots_{0}.jpg".format(folder_n, i))
        image = camogen.generate(color_param)
        image.save("./foreground{0}/foreground_blots_{1}.jpg".format(folder_n, i))
        print("./foreground{0}/foreground_blots_{1}.jpg".format(folder_n, i))
        i += 1