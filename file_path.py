def path(lattice,  beta, order):
    if lattice == "triangular":
        if beta == 0.8:
            return "/mnt/data/GammaBK_triangular/Gamma_BK/Beta0.8/Beta0.8_Order{0}/Weight".format(order)
        elif beta == 1.0:
            return "/mnt/data/GammaBK_triangular/Gamma_BK/Beta1.0/Beta1.0_Order{0}/Weight".format(order)
        elif beta == 1.5:
            return "/mnt/data/GammaBK_triangular/Gamma_BK/Beta1.5/Beta1.5_Order{0}/Weight".format(order)
    elif lattice == "square":
        if beta == 0.8:
            if order == 1:
                return "/mnt/data/GammaBK_square/Beta0.8/Beta0.8_Tau32_L8/Weight"
            else:
                return "/mnt/data/GammaBK_square/Beta0.8/Beta0.8_Order{}/Weight".format(order)
        elif beta == 1.0:
            return "/mnt/data/GammaBK_square/Beta1.0/Beta1.0_Order{}/Weight".format(order)
            # return "./square/Beta1.0_Order{}_Tau32_L8_Weight".format(order)
    elif lattice == "J1J2":
        if beta == 1.0:
            return "/mnt/data/GammaBK_J1J2/Beta1.0/Beta1.0_Order{}/Weight".format(order)
        elif beta == 1.5:
            return "/mnt/data/GammaBK_J1J2/Beta1.5/Beta1.5_Order{}/Weight".format(order)




