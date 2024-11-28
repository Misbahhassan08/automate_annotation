import xml.etree.ElementTree as ET

class xml_builder:
    
    def __init__(self, project_path):
        self.directory = project_path
        pass # end of init function 
    
    def update_xml_file(self,image_path,xml_path, width, height , xmin, ymin, xmax, ymax, label_class_name):
        dict = []
        tree = ET.parse(xml_path)
        root = tree.getroot()
       
        #annoataion = root.find('annotation')
        print(root.tag, root.text)

        object = ET.SubElement(root, 'object')
        name = ET.SubElement(object, 'name')
        name.text = label_class_name
        pose = ET.SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = ET.SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = ET.SubElement(object, 'difficult')
        difficult.text = '0'
        # bounding_box
        bndbox = ET.SubElement(object, 'bndbox')
        x_min = ET.SubElement(bndbox, 'xmin')
        x_min.text = f'{xmin}'
        y_min = ET.SubElement(bndbox, 'ymin')
        y_min.text = f'{ymin}'
        x_max = ET.SubElement(bndbox, 'xmax')
        x_max.text = f'{xmax}'
        y_max = ET.SubElement(bndbox, 'ymax')
        y_max.text = f'{ymax}'
        
        # for child in root.find('object'):
        #     print(child.tag, child.text)
        #     if child.tag == 'bndbox':
        #         for grandchild in child:
        #             print(grandchild.tag, grandchild.text)
        save_path_file = xml_path

        ET.indent(tree, space="\t", level=0)
        tree.write(save_path_file, encoding="utf-8")
            
        pass # end of function update_xml_file

    def build_xml_file(self,image_path,xml_path, width, height , xmin, ymin, xmax, ymax, label_class_name):
        annoataion = ET.Element('annotation')
        folder = ET.SubElement(annoataion, 'folder')
        folder.text = 'JPEGImages'
        filename = ET.SubElement(annoataion, 'filename')
        filename.text = 'file1.png'
        path = ET.SubElement(annoataion, 'path')
        path.text= f'{image_path}' #r'E:\Anotation\annotation medicine\JPEGImages\file1.png'

        source = ET.SubElement(annoataion, 'source')
        database = ET.SubElement(source, 'database')
        database.text = 'Unknown'


        size = ET.SubElement(annoataion, 'size')
        width = ET.SubElement(size, 'width')
        width.text = f'{width}'
        height = ET.SubElement(size, 'height')
        height.text = f'{height}'
        depth = ET.SubElement(size, 'depth')
        depth.text = '3'

        segmented = ET.SubElement(annoataion, 'segmented')
        segmented.text = '0'

        object = ET.SubElement(annoataion, 'object')
        name = ET.SubElement(object, 'name')
        name.text = label_class_name
        pose = ET.SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = ET.SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = ET.SubElement(object, 'difficult')
        difficult.text = '0'
        # bounding_box
        bndbox = ET.SubElement(object, 'bndbox')
        x_min = ET.SubElement(bndbox, 'xmin')
        x_min.text = f'{xmin}'
        y_min = ET.SubElement(bndbox, 'ymin')
        y_min.text = f'{ymin}'
        x_max = ET.SubElement(bndbox, 'xmax')
        x_max.text = f'{xmax}'
        y_max = ET.SubElement(bndbox, 'ymax')
        y_max.text = f'{ymax}'

        tree = ET.ElementTree(annoataion)

        save_path_file = xml_path

        ET.indent(tree, space="\t", level=0)
        tree.write(save_path_file, encoding="utf-8")
        
        pass # end of build xml function
    pass # end of class xml builder  

if __name__ == '__main__':
    import os 

    model_name = 'pills'
    project_path = os.getcwd()
    frame_number = 1

    xml_path = f"{project_path}/data/{model_name}/Annotations/file{frame_number}.xml"

    myxml = xml_builder(project_path)
    myxml.update_xml_file(xml_path)
    pass # unit test 