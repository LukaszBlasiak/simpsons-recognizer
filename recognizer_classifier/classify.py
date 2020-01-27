import tensorflow as tf
import sys
import os
import cv2


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf



label_lines = [line.rstrip() for line
               in tf.gfile.GFile("tf_files/retrained_labels.txt")]

with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def,
                            name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    while True:
        for dirpath, _, filenames in os.walk('../backend/images_workspace/'):
            for f in filenames:
                file_path = os.path.abspath(os.path.join(dirpath, f))
                if not os.path.isdir(file_path) and file_path.find('-to_recognize') != -1:
                    # image = cv2.imread(file_path)
                    image_data = tf.gfile.FastGFile(file_path, 'rb').read()

                    predictions = sess.run(softmax_tensor,
                                           {'DecodeJpeg/contents:0': image_data})
                    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

                    for node_id in top_k:
                        human_string = label_lines[node_id]
                        score = predictions[0][node_id]
                        print('%s (score = %.5f)' % (human_string, score))

                    # All the results have been drawn on image. Now display the image.
                    save_file_path = os.path.abspath(os.path.join(dirpath, 'recognized', f))
                    save_file_path = save_file_path.replace('-to_recognize', '-recognized', 1)

                    #dodanie etykiety
                    image = cv2.imread(file_path)
                    label_text = "Found: " + label_lines[top_k[0]].upper() + " conf: " + str(round(predictions[0][top_k[0]],3))
                    image = cv2.putText(image, label_text, (00,20), cv2.FONT_HERSHEY_COMPLEX , 0.6, (255, 255, 255), 1, lineType=cv2.LINE_AA)
                    cv2.imwrite(save_file_path, image)
                    os.remove(file_path)
        cv2.waitKey(1000)
