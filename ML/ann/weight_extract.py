#Extract weights from model and store in file in easily readable format and return file object
def get_weights(model):
    #Create New Text File with Weights and erase any existing file with same name
    file_obj = open("model weights","w")
    file_obj.write("Formatted Output:\n\n")
    #Output formatted data for easy visual analysis
    for layer in range(0,len(model.layers)):
        file_obj.write("Layer %d -> Layer %d Weights:\n\t   " % (layer, layer+1))
        layer_weights = model.layers[layer].get_weights()
        #Print top labels
        next_node_num = 0
        for next_layer_node_num in range(0,len(layer_weights[0][0])):
            file_obj.write("     L:%d N:%d" % (layer+1,next_node_num))
            next_node_num += 1
        file_obj.write("\n")
        #First print node weights
        for node in range(0,len(layer_weights[0])):
            file_obj.write("L:%d N:%d: " % (layer,node))
            for node_weight in layer_weights[0][node]:
                file_obj.write("  % 6.5f  " % node_weight)
            file_obj.write("\n")
        #Next print bias weights
        file_obj.write("\nL:%d Bias: " % (layer+1))
        for node in layer_weights[1]:
            file_obj.write("  % 6.5f  " % node)
        file_obj.write("\n\n")
    #Output raw data for easy parsing later
    file_obj.write("\n\nUnformatted Output for Parsing:\nz")
    for layer in range(0,len(model.layers)):
        weight_layer = model.layers[layer].get_weights()
        print(weight_layer)
        #First Take Care of node weights
        for node_list in range(0,len(weight_layer[0])):
            for node in range(0,len(weight_layer[0][node_list])):
                file_obj.write("%.8f" % weight_layer[0][node_list][node])
                if node < len(weight_layer[0][node_list])-1:
                    file_obj.write("x")
            if node_list < len(weight_layer[0])-1:
                file_obj.write("y")
        file_obj.write("z")
        #Next Take Care of bias weights
        for bias in range(0,len(weight_layer[1])):
            file_obj.write("%.8f" % weight_layer[1][bias])
            if bias < len(weight_layer[1])-1:
                file_obj.write("x")
        if layer < len(model.layers)-1:
            file_obj.write("z")
    file_obj.close()
    return open("model weights", "r")

#Extract weights from file object and set model weights and returns updated model
def set_weights(fileobj,model):
    start_parsing = False
    parse_list = []
    temp_list = []
    weight_type = 0
    for line in fileobj.read().split("z")[1:]:
        #Take care of node weights first
        if weight_type == 0:
            node_temp = []
            node_list = line.split("y")
            for sub_list in node_list:
                node_temp.append(sub_list.split("x"))
            temp_list.append(np.array(node_temp,dtype=np.float32))
            weight_type = 1
        elif weight_type == 1:
            #Take Care of Bias weights
            temp_list.append(np.array(line.split("x"), dtype=np.float32))
            parse_list.append(temp_list)
            temp_list = []
            weight_type = 0
    for layer in range(0,len(model.layers)):
        model.layers[layer].set_weights(parse_list[layer])
    return model
