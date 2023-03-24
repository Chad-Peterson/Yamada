from yamada import SpatialGraph
import numpy as np

nodes = ['7939',
         '2640',
         '3040',
         '3440',
         '3840',
         '4240',
         '4640',
         '5040',
         '5440',
         '7945',
         '7941',
         '1858',
         '1838',
         '1818',
         '1798',
         '1778',
         '1758',
         '1738',
         '1718',
         '1698',
         '2062',
         '2042',
         '2422',
         '2802',
         '3181',
         '3201',
         '3221',
         '2842',
         '2463',
         '2484',
         '2505',
         '2126',
         '2147',
         '2167',
         '2188',
         '2208',
         '2228',
         '1865',
         '7953',
         '7938',
         '1642',
         '1643',
         '1644',
         '1645',
         '1646',
         '1647',
         '1648',
         '1649',
         '7950',
         '7949',
         '1687',
         '1707',
         '1727',
         '1747',
         '1767',
         '1787',
         '1807',
         '1827',
         '7952',
         '7943',
         '6060',
         '6080',
         '6100',
         '6120',
         '6140',
         '6160',
         '6180',
         '6200',
         '7946',
         '7944',
         '6022',
         '6023',
         '6024',
         '6025',
         '6026',
         '6027',
         '6028',
         '6029',
         '7956',
         '7948',
         '2431',
         '2451',
         '2470',
         '2490',
         '2510',
         '2529',
         '2549',
         '2569',
         '2588',
         '2608',
         '2628',
         '2648',
         '2267',
         '2647',
         '2627',
         '3007',
         '3387',
         '3767',
         '4148',
         '4529',
         '4509',
         '4889',
         '4870',
         '5251',
         '5231',
         '7954',
         '7951',
         '2651',
         '3051',
         '3451',
         '3851',
         '4251',
         '4651',
         '5051',
         '5451',
         '7957',
         '7936',
         '2420',
         '2421',
         '2822',
         '2823',
         '3224',
         '3625',
         '4026',
         '4427',
         '4828',
         '5229',
         '5650',
         '5651',
         '6072',
         '5671',
         '5670',
         '5669',
         '5668',
         '5667',
         '5666',
         '5665',
         '5664',
         '5243',
         '5242',
         '5221',
         '5220',
         '7942',
         '7955',
         '6071',
         '6091',
         '6111',
         '6131',
         '6151',
         '6171',
         '6191',
         '6211',
         '7958',
         '7937',
         '1676',
         '1697',
         '1333',
         '970',
         '991',
         '1012',
         '1032',
         '669',
         '689',
         '688',
         '1071',
         '1454',
         '1817',
         '1816',
         '7940',
         '7947',
         '6242',
         '6223',
         '6204',
         '6185',
         '6165',
         '6146',
         '6127',
         '5708',
         '5689',
         '5270',
         '4850',
         '4431',
         '4451',
         '4471',
         '4491',
         '4511',
         '4531',
         '4950',
         '5370',
         '5789',
         '6209',
         '6229',
         '6249',
         '7959']

node_positions = [np.array([30., 80., 20.]),
 np.array([31.57894737, 78.94736842, 21.05263158]),
 np.array([36.84210526, 78.94736842, 21.05263158]),
 np.array([42.10526316, 78.94736842, 21.05263158]),
 np.array([47.36842105, 78.94736842, 21.05263158]),
 np.array([52.63157895, 78.94736842, 21.05263158]),
 np.array([57.89473684, 78.94736842, 21.05263158]),
 np.array([63.15789474, 78.94736842, 21.05263158]),
 np.array([68.42105263, 78.94736842, 21.05263158]),
 np.array([70., 80., 20.]),
 np.array([20., 80., 30.]),
 np.array([21.05263158, 78.94736842, 31.57894737]),
 np.array([21.05263158, 73.68421053, 31.57894737]),
 np.array([21.05263158, 68.42105263, 31.57894737]),
 np.array([21.05263158, 63.15789474, 31.57894737]),
 np.array([21.05263158, 57.89473684, 31.57894737]),
 np.array([21.05263158, 52.63157895, 31.57894737]),
 np.array([21.05263158, 47.36842105, 31.57894737]),
 np.array([21.05263158, 42.10526316, 31.57894737]),
 np.array([21.05263158, 36.84210526, 31.57894737]),
 np.array([26.31578947, 31.57894737, 31.57894737]),
 np.array([26.31578947, 26.31578947, 31.57894737]),
 np.array([31.57894737, 21.05263158, 31.57894737]),
 np.array([36.84210526, 15.78947368, 31.57894737]),
 np.array([42.10526316, 10.52631579, 26.31578947]),
 np.array([42.10526316, 15.78947368, 26.31578947]),
 np.array([42.10526316, 21.05263158, 26.31578947]),
 np.array([36.84210526, 26.31578947, 31.57894737]),
 np.array([31.57894737, 31.57894737, 36.84210526]),
 np.array([31.57894737, 36.84210526, 42.10526316]),
 np.array([31.57894737, 42.10526316, 47.36842105]),
 np.array([26.31578947, 47.36842105, 52.63157895]),
 np.array([26.31578947, 52.63157895, 57.89473684]),
 np.array([26.31578947, 57.89473684, 57.89473684]),
 np.array([26.31578947, 63.15789474, 63.15789474]),
 np.array([26.31578947, 68.42105263, 63.15789474]),
 np.array([26.31578947, 73.68421053, 63.15789474]),
 np.array([21.05263158, 78.94736842, 68.42105263]),
 np.array([20., 80., 70.]),
 np.array([20., 20., 30.]),
 np.array([21.05263158, 21.05263158, 31.57894737]),
 np.array([21.05263158, 21.05263158, 36.84210526]),
 np.array([21.05263158, 21.05263158, 42.10526316]),
 np.array([21.05263158, 21.05263158, 47.36842105]),
 np.array([21.05263158, 21.05263158, 52.63157895]),
 np.array([21.05263158, 21.05263158, 57.89473684]),
 np.array([21.05263158, 21.05263158, 63.15789474]),
 np.array([21.05263158, 21.05263158, 68.42105263]),
 np.array([20., 20., 70.]),
 np.array([20., 30., 80.]),
 np.array([21.05263158, 31.57894737, 78.94736842]),
 np.array([21.05263158, 36.84210526, 78.94736842]),
 np.array([21.05263158, 42.10526316, 78.94736842]),
 np.array([21.05263158, 47.36842105, 78.94736842]),
 np.array([21.05263158, 52.63157895, 78.94736842]),
 np.array([21.05263158, 57.89473684, 78.94736842]),
 np.array([21.05263158, 63.15789474, 78.94736842]),
 np.array([21.05263158, 68.42105263, 78.94736842]),
 np.array([20., 70., 80.]),
 np.array([80., 30., 20.]),
 np.array([78.94736842, 31.57894737, 21.05263158]),
 np.array([78.94736842, 36.84210526, 21.05263158]),
 np.array([78.94736842, 42.10526316, 21.05263158]),
 np.array([78.94736842, 47.36842105, 21.05263158]),
 np.array([78.94736842, 52.63157895, 21.05263158]),
 np.array([78.94736842, 57.89473684, 21.05263158]),
 np.array([78.94736842, 63.15789474, 21.05263158]),
 np.array([78.94736842, 68.42105263, 21.05263158]),
 np.array([80., 70., 20.]),
 np.array([80., 20., 30.]),
 np.array([78.94736842, 21.05263158, 31.57894737]),
 np.array([78.94736842, 21.05263158, 36.84210526]),
 np.array([78.94736842, 21.05263158, 42.10526316]),
 np.array([78.94736842, 21.05263158, 47.36842105]),
 np.array([78.94736842, 21.05263158, 52.63157895]),
 np.array([78.94736842, 21.05263158, 57.89473684]),
 np.array([78.94736842, 21.05263158, 63.15789474]),
 np.array([78.94736842, 21.05263158, 68.42105263]),
 np.array([80., 20., 70.]),
 np.array([30., 20., 80.]),
 np.array([31.57894737, 21.05263158, 78.94736842]),
 np.array([31.57894737, 26.31578947, 78.94736842]),
 np.array([31.57894737, 31.57894737, 73.68421053]),
 np.array([31.57894737, 36.84210526, 73.68421053]),
 np.array([31.57894737, 42.10526316, 73.68421053]),
 np.array([31.57894737, 47.36842105, 68.42105263]),
 np.array([31.57894737, 52.63157895, 68.42105263]),
 np.array([31.57894737, 57.89473684, 68.42105263]),
 np.array([31.57894737, 63.15789474, 63.15789474]),
 np.array([31.57894737, 68.42105263, 63.15789474]),
 np.array([31.57894737, 73.68421053, 63.15789474]),
 np.array([31.57894737, 78.94736842, 63.15789474]),
 np.array([26.31578947, 84.21052632, 57.89473684]),
 np.array([31.57894737, 78.94736842, 57.89473684]),
 np.array([31.57894737, 73.68421053, 57.89473684]),
 np.array([36.84210526, 68.42105263, 57.89473684]),
 np.array([42.10526316, 63.15789474, 57.89473684]),
 np.array([47.36842105, 57.89473684, 57.89473684]),
 np.array([52.63157895, 52.63157895, 63.15789474]),
 np.array([57.89473684, 47.36842105, 68.42105263]),
 np.array([57.89473684, 42.10526316, 68.42105263]),
 np.array([63.15789474, 36.84210526, 68.42105263]),
 np.array([63.15789474, 31.57894737, 73.68421053]),
 np.array([68.42105263, 26.31578947, 78.94736842]),
 np.array([68.42105263, 21.05263158, 78.94736842]),
 np.array([70., 20., 80.]),
 np.array([30., 80., 80.]),
 np.array([31.57894737, 78.94736842, 78.94736842]),
 np.array([36.84210526, 78.94736842, 78.94736842]),
 np.array([42.10526316, 78.94736842, 78.94736842]),
 np.array([47.36842105, 78.94736842, 78.94736842]),
 np.array([52.63157895, 78.94736842, 78.94736842]),
 np.array([57.89473684, 78.94736842, 78.94736842]),
 np.array([63.15789474, 78.94736842, 78.94736842]),
 np.array([68.42105263, 78.94736842, 78.94736842]),
 np.array([70., 80., 80.]),
 np.array([30., 20., 20.]),
 np.array([31.57894737, 21.05263158, 21.05263158]),
 np.array([31.57894737, 21.05263158, 26.31578947]),
 np.array([36.84210526, 21.05263158, 31.57894737]),
 np.array([36.84210526, 21.05263158, 36.84210526]),
 np.array([42.10526316, 21.05263158, 42.10526316]),
 np.array([47.36842105, 21.05263158, 47.36842105]),
 np.array([52.63157895, 21.05263158, 52.63157895]),
 np.array([57.89473684, 21.05263158, 57.89473684]),
 np.array([63.15789474, 21.05263158, 63.15789474]),
 np.array([68.42105263, 21.05263158, 68.42105263]),
 np.array([73.68421053, 26.31578947, 73.68421053]),
 np.array([73.68421053, 26.31578947, 78.94736842]),
 np.array([78.94736842, 31.57894737, 84.21052632]),
 np.array([73.68421053, 31.57894737, 78.94736842]),
 np.array([73.68421053, 31.57894737, 73.68421053]),
 np.array([73.68421053, 31.57894737, 68.42105263]),
 np.array([73.68421053, 31.57894737, 63.15789474]),
 np.array([73.68421053, 31.57894737, 57.89473684]),
 np.array([73.68421053, 31.57894737, 52.63157895]),
 np.array([73.68421053, 31.57894737, 47.36842105]),
 np.array([73.68421053, 31.57894737, 42.10526316]),
 np.array([68.42105263, 26.31578947, 36.84210526]),
 np.array([68.42105263, 26.31578947, 31.57894737]),
 np.array([68.42105263, 21.05263158, 26.31578947]),
 np.array([68.42105263, 21.05263158, 21.05263158]),
 np.array([70., 20., 20.]),
 np.array([80., 30., 80.]),
 np.array([78.94736842, 31.57894737, 78.94736842]),
 np.array([78.94736842, 36.84210526, 78.94736842]),
 np.array([78.94736842, 42.10526316, 78.94736842]),
 np.array([78.94736842, 47.36842105, 78.94736842]),
 np.array([78.94736842, 52.63157895, 78.94736842]),
 np.array([78.94736842, 57.89473684, 78.94736842]),
 np.array([78.94736842, 63.15789474, 78.94736842]),
 np.array([78.94736842, 68.42105263, 78.94736842]),
 np.array([80., 70., 80.]),
 np.array([20., 30., 20.]),
 np.array([21.05263158, 31.57894737, 21.05263158]),
 np.array([21.05263158, 36.84210526, 26.31578947]),
 np.array([15.78947368, 42.10526316, 26.31578947]),
 np.array([10.52631579, 47.36842105, 31.57894737]),
 np.array([10.52631579, 52.63157895, 36.84210526]),
 np.array([10.52631579, 57.89473684, 42.10526316]),
 np.array([10.52631579, 63.15789474, 42.10526316]),
 np.array([ 5.26315789, 68.42105263, 47.36842105]),
 np.array([ 5.26315789, 73.68421053, 47.36842105]),
 np.array([ 5.26315789, 73.68421053, 42.10526316]),
 np.array([10.52631579, 73.68421053, 36.84210526]),
 np.array([15.78947368, 73.68421053, 31.57894737]),
 np.array([21.05263158, 68.42105263, 26.31578947]),
 np.array([21.05263158, 68.42105263, 21.05263158]),
 np.array([20., 70., 20.]),
 np.array([80., 80., 30.]),
 np.array([78.94736842, 78.94736842, 31.57894737]),
 np.array([78.94736842, 73.68421053, 36.84210526]),
 np.array([78.94736842, 68.42105263, 42.10526316]),
 np.array([78.94736842, 63.15789474, 47.36842105]),
 np.array([78.94736842, 57.89473684, 47.36842105]),
 np.array([78.94736842, 52.63157895, 52.63157895]),
 np.array([78.94736842, 47.36842105, 57.89473684]),
 np.array([73.68421053, 42.10526316, 63.15789474]),
 np.array([73.68421053, 36.84210526, 68.42105263]),
 np.array([68.42105263, 31.57894737, 73.68421053]),
 np.array([63.15789474, 26.31578947, 73.68421053]),
 np.array([57.89473684, 21.05263158, 78.94736842]),
 np.array([57.89473684, 26.31578947, 78.94736842]),
 np.array([57.89473684, 31.57894737, 78.94736842]),
 np.array([57.89473684, 36.84210526, 78.94736842]),
 np.array([57.89473684, 42.10526316, 78.94736842]),
 np.array([57.89473684, 47.36842105, 78.94736842]),
 np.array([63.15789474, 52.63157895, 73.68421053]),
 np.array([68.42105263, 57.89473684, 73.68421053]),
 np.array([73.68421053, 63.15789474, 68.42105263]),
 np.array([78.94736842, 68.42105263, 68.42105263]),
 np.array([78.94736842, 73.68421053, 68.42105263]),
 np.array([78.94736842, 78.94736842, 68.42105263]),
 np.array([80., 80., 70.])]

edges = [('7939', '2640'),
 ('2640', '3040'),
 ('3040', '3440'),
 ('3440', '3840'),
 ('3840', '4240'),
 ('4240', '4640'),
 ('4640', '5040'),
 ('5040', '5440'),
 ('5440', '7945'),
 ('7941', '1858'),
 ('1858', '1838'),
 ('1838', '1818'),
 ('1818', '1798'),
 ('1798', '1778'),
 ('1778', '1758'),
 ('1758', '1738'),
 ('1738', '1718'),
 ('1718', '1698'),
 ('1698', '2062'),
 ('2062', '2042'),
 ('2042', '2422'),
 ('2422', '2802'),
 ('2802', '3181'),
 ('3181', '3201'),
 ('3201', '3221'),
 ('3221', '2842'),
 ('2842', '2463'),
 ('2463', '2484'),
 ('2484', '2505'),
 ('2505', '2126'),
 ('2126', '2147'),
 ('2147', '2167'),
 ('2167', '2188'),
 ('2188', '2208'),
 ('2208', '2228'),
 ('2228', '1865'),
 ('1865', '7953'),
 ('7938', '1642'),
 ('1642', '1643'),
 ('1643', '1644'),
 ('1644', '1645'),
 ('1645', '1646'),
 ('1646', '1647'),
 ('1647', '1648'),
 ('1648', '1649'),
 ('1649', '7950'),
 ('7949', '1687'),
 ('1687', '1707'),
 ('1707', '1727'),
 ('1727', '1747'),
 ('1747', '1767'),
 ('1767', '1787'),
 ('1787', '1807'),
 ('1807', '1827'),
 ('1827', '7952'),
 ('7943', '6060'),
 ('6060', '6080'),
 ('6080', '6100'),
 ('6100', '6120'),
 ('6120', '6140'),
 ('6140', '6160'),
 ('6160', '6180'),
 ('6180', '6200'),
 ('6200', '7946'),
 ('7944', '6022'),
 ('6022', '6023'),
 ('6023', '6024'),
 ('6024', '6025'),
 ('6025', '6026'),
 ('6026', '6027'),
 ('6027', '6028'),
 ('6028', '6029'),
 ('6029', '7956'),
 ('7948', '2431'),
 ('2431', '2451'),
 ('2451', '2470'),
 ('2470', '2490'),
 ('2490', '2510'),
 ('2510', '2529'),
 ('2529', '2549'),
 ('2549', '2569'),
 ('2569', '2588'),
 ('2588', '2608'),
 ('2608', '2628'),
 ('2628', '2648'),
 ('2648', '2267'),
 ('2267', '2647'),
 ('2647', '2627'),
 ('2627', '3007'),
 ('3007', '3387'),
 ('3387', '3767'),
 ('3767', '4148'),
 ('4148', '4529'),
 ('4529', '4509'),
 ('4509', '4889'),
 ('4889', '4870'),
 ('4870', '5251'),
 ('5251', '5231'),
 ('5231', '7954'),
 ('7951', '2651'),
 ('2651', '3051'),
 ('3051', '3451'),
 ('3451', '3851'),
 ('3851', '4251'),
 ('4251', '4651'),
 ('4651', '5051'),
 ('5051', '5451'),
 ('5451', '7957'),
 ('7936', '2420'),
 ('2420', '2421'),
 ('2421', '2822'),
 ('2822', '2823'),
 ('2823', '3224'),
 ('3224', '3625'),
 ('3625', '4026'),
 ('4026', '4427'),
 ('4427', '4828'),
 ('4828', '5229'),
 ('5229', '5650'),
 ('5650', '5651'),
 ('5651', '6072'),
 ('6072', '5671'),
 ('5671', '5670'),
 ('5670', '5669'),
 ('5669', '5668'),
 ('5668', '5667'),
 ('5667', '5666'),
 ('5666', '5665'),
 ('5665', '5664'),
 ('5664', '5243'),
 ('5243', '5242'),
 ('5242', '5221'),
 ('5221', '5220'),
 ('5220', '7942'),
 ('7955', '6071'),
 ('6071', '6091'),
 ('6091', '6111'),
 ('6111', '6131'),
 ('6131', '6151'),
 ('6151', '6171'),
 ('6171', '6191'),
 ('6191', '6211'),
 ('6211', '7958'),
 ('7937', '1676'),
 ('1676', '1697'),
 ('1697', '1333'),
 ('1333', '970'),
 ('970', '991'),
 ('991', '1012'),
 ('1012', '1032'),
 ('1032', '669'),
 ('669', '689'),
 ('689', '688'),
 ('688', '1071'),
 ('1071', '1454'),
 ('1454', '1817'),
 ('1817', '1816'),
 ('1816', '7940'),
 ('7947', '6242'),
 ('6242', '6223'),
 ('6223', '6204'),
 ('6204', '6185'),
 ('6185', '6165'),
 ('6165', '6146'),
 ('6146', '6127'),
 ('6127', '5708'),
 ('5708', '5689'),
 ('5689', '5270'),
 ('5270', '4850'),
 ('4850', '4431'),
 ('4431', '4451'),
 ('4451', '4471'),
 ('4471', '4491'),
 ('4491', '4511'),
 ('4511', '4531'),
 ('4531', '4950'),
 ('4950', '5370'),
 ('5370', '5789'),
 ('5789', '6209'),
 ('6209', '6229'),
 ('6229', '6249'),
 ('6249', '7959'),
 ('7938', '7936'),
 ('7938', '7937'),
 ('7941', '7939'),
 ('7941', '7940'),
 ('7944', '7942'),
 ('7944', '7943'),
 ('7947', '7945'),
 ('7947', '7946'),
 ('7950', '7948'),
 ('7950', '7949'),
 ('7953', '7951'),
 ('7953', '7952'),
 ('7956', '7954'),
 ('7956', '7955'),
 ('7959', '7957'),
 ('7959', '7958')]


sg = SpatialGraph(nodes=nodes, edges=edges, node_positions=node_positions)

sg.plot()

sgd = sg.create_spatial_graph_diagram()

yp = sgd.normalized_yamada_polynomial()

print("Yamada polynomial: {}".format(yp))