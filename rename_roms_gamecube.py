import os, glob, shutil, pathlib

roms_path = "E:\\games"
mode = 0 #0 to gamecube nintendont, 1 = to gamecube isos, 2 = strip names

match mode:
    case 0:
        list_games = glob.glob(roms_path + "\\*.iso")

        for game in list_games:
            folder_name = game.replace(".iso", "").replace(" - Disc 2" , "")
            if(not os.path.exists(folder_name)):
                os.makedirs(folder_name)
            
            game_basename = os.path.basename(game)

            if(game_basename.endswith("Disc 2.iso")):
                shutil.move(game, folder_name + "\\disc2.iso")
            else:
                shutil.move(game, folder_name + "\\game.iso")
    case 1:
        list_paths = os.listdir(roms_path)
        for path in list_paths:
            if(os.path.isfile(os.path.join(roms_path, path))):
                continue
            else:
                fullpath_disc1 = os.path.join(roms_path, path, "game.iso")
                fullpath_disc2 = os.path.join(roms_path, path, "disc2.iso")
                fullpath_dest_disc1 = roms_path + "\\" + path + ".iso"
                fullpath_dest_disc2 = roms_path + "\\" + path + " - Disc 2.iso"

                if(os.path.exists(fullpath_disc1)):
                    os.replace(fullpath_disc1, fullpath_dest_disc1)
        
                    if(os.path.exists(fullpath_disc2)):
                        os.replace(fullpath_disc2, fullpath_dest_disc2)

                    shutil.rmtree(os.path.join(roms_path, path))
                    # os.remove(os.path.join(roms_path, path))
                
    case 2:
        list_games = glob.glob(roms_path + "\\*.iso")
        for game_name in list_games:
            try:
                index_remove = game_name.index("(")
                if(os.path.exists(game_name[0:index_remove].strip() + ".iso")):
                    os.rename(game_name, game_name[0:index_remove].strip() + " - Disc 2.iso")
                else:    
                    os.rename(game_name, game_name[0:index_remove].strip() + ".iso")
            except: pass
