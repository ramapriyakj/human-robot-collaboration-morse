
import os

import six.moves.urllib.request as request
import tensorflow as tf

# Check that we have correct TensorFlow version installed
tf_version = tf.__version__
print("TensorFlow version: {}".format(tf_version))
assert "1.4" <= tf_version, "TensorFlow r1.4 or later is needed"

PATH = "/home/amal/robotics/morsetrainingr30"

FILE_TRAIN = "/home/amal/robotics/morsetrainingr30/training.csv"
tf.logging.set_verbosity(tf.logging.INFO)

feature_names = [
'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20', 'm21', 'm22', 'm23', 'm24', 'm25', 'm26', 'm27', 'm28', 'm29', 'm30', 'm31', 'm32', 'm33', 'm34', 'm35', 'm36', 'm37', 'm38', 'm39', 'm40', 'm41', 'm42', 'm43', 'm44', 'm45', 'm46', 'm47', 'm48', 'm49', 'm50', 'm51', 'm52', 'm53', 'm54', 'm55', 'm56', 'm57', 'm58', 'm59', 'm60', 'm61', 'm62', 'm63', 'm64', 'm65', 'm66', 'm67', 'm68', 'm69', 'm70', 'm71', 'm72', 'm73', 'm74', 'm75', 'm76', 'm77', 'm78', 'm79', 'm80', 'm81', 'm82', 'm83', 'm84', 'm85', 'm86', 'm87', 'm88', 'm89', 'm90', 'm91', 'm92', 'm93', 'm94', 'm95', 'm96', 'm97', 'm98', 'm99', 'm100', 'm101', 'm102', 'm103', 'm104', 'm105', 'm106', 'm107', 'm108', 'm109', 'm110', 'm111', 'm112', 'm113', 'm114', 'm115', 'm116', 'm117', 'm118', 'm119', 'm120', 'm121', 'm122', 'm123', 'm124', 'm125', 'm126', 'm127', 'm128', 'm129', 'm130', 'm131', 'm132', 'm133', 'm134', 'm135', 'm136', 'm137', 'm138', 'm139', 'm140', 'm141', 'm142', 'm143', 'm144', 'm145', 'm146', 'm147', 'm148', 'm149', 'm150', 'm151', 'm152', 'm153', 'm154', 'm155', 'm156', 'm157', 'm158', 'm159', 'm160', 'm161', 'm162', 'm163', 'm164', 'm165', 'm166', 'm167', 'm168', 'm169', 'm170', 'm171', 'm172', 'm173', 'm174', 'm175', 'm176', 'm177', 'm178', 'm179', 'm180', 'm181', 'm182', 'm183', 'm184', 'm185', 'm186', 'm187', 'm188', 'm189', 'm190', 'm191', 'm192', 'm193', 'm194', 'm195', 'm196', 'm197', 'm198', 'm199', 'm200', 
'm201', 'm202', 'm203', 'm204', 'm205', 'm206', 'm207', 'm208', 'm209', 'm210', 'm211', 'm212', 'm213', 'm214', 'm215', 'm216', 'm217', 'm218', 'm219', 'm220', 'm221', 'm222', 'm223', 'm224', 'm225', 'm226', 'm227', 'm228', 'm229', 'm230', 'm231', 'm232', 'm233', 'm234', 'm235', 'm236', 'm237', 'm238', 'm239', 'm240', 'm241', 'm242', 'm243', 'm244', 'm245', 'm246', 'm247', 'm248', 'm249', 'm250', 'm251', 'm252', 'm253', 'm254', 'm255', 'm256', 'm257', 'm258', 'm259', 'm260', 'm261', 'm262', 'm263', 'm264', 'm265', 'm266', 'm267', 'm268', 'm269', 'm270', 'm271', 'm272', 'm273', 'm274', 'm275', 'm276', 'm277', 'm278', 'm279', 'm280', 'm281', 'm282', 'm283', 'm284', 'm285', 'm286', 'm287', 'm288', 'm289', 'm290', 'm291', 'm292', 'm293', 'm294', 'm295', 'm296', 'm297', 'm298', 'm299', 'm300', 'm301', 'm302', 'm303', 'm304', 'm305', 'm306', 'm307', 'm308', 'm309', 'm310', 'm311', 'm312', 'm313', 'm314', 'm315', 'm316', 'm317', 'm318', 'm319', 'm320', 'm321', 'm322', 'm323', 'm324', 'm325', 'm326', 'm327', 'm328', 'm329', 'm330', 'm331', 'm332', 'm333', 'm334', 'm335', 'm336', 'm337', 'm338', 'm339', 'm340', 'm341', 'm342', 'm343', 'm344', 'm345', 'm346', 'm347', 'm348', 'm349', 'm350', 'm351', 'm352', 'm353', 'm354', 'm355', 'm356', 'm357', 'm358', 'm359', 'm360', 'm361', 'm362', 'm363', 'm364', 'm365', 'm366', 'm367', 'm368', 'm369', 'm370', 'm371', 'm372', 'm373', 'm374', 'm375', 'm376', 'm377', 'm378', 'm379', 'm380', 'm381', 'm382', 'm383', 'm384', 'm385', 'm386', 'm387', 'm388', 'm389', 'm390', 'm391', 'm392', 'm393', 'm394', 'm395', 'm396', 'm397', 'm398', 'm399', 'm400', 
'm401', 'm402', 'm403', 'm404', 'm405', 'm406', 'm407', 'm408', 'm409', 'm410', 'm411', 'm412', 'm413', 'm414', 'm415', 'm416', 'm417', 'm418', 'm419', 'm420', 'm421', 'm422', 'm423', 'm424', 'm425', 'm426', 'm427', 'm428', 'm429', 'm430', 'm431', 'm432', 'm433', 'm434', 'm435', 'm436', 'm437', 'm438', 'm439', 'm440', 'm441', 'm442', 'm443', 'm444', 'm445', 'm446', 'm447', 'm448', 'm449', 'm450', 'm451', 'm452', 'm453', 'm454', 'm455', 'm456', 'm457', 'm458', 'm459', 'm460', 'm461', 'm462', 'm463', 'm464', 'm465', 'm466', 'm467', 'm468', 'm469', 'm470', 'm471', 'm472', 'm473', 'm474', 'm475', 'm476', 'm477', 'm478', 'm479', 'm480', 'm481', 'm482', 'm483', 'm484', 'm485', 'm486', 'm487', 'm488', 'm489', 'm490', 'm491', 'm492', 'm493', 'm494', 'm495', 'm496', 'm497', 'm498', 'm499', 'm500', 'm501', 'm502', 'm503', 'm504', 'm505', 'm506', 'm507', 'm508', 'm509', 'm510', 'm511', 'm512', 'm513', 'm514', 'm515', 'm516', 'm517', 'm518', 'm519', 'm520', 'm521', 'm522', 'm523', 'm524', 'm525', 'm526', 'm527', 'm528', 'm529', 'm530', 'm531', 'm532', 'm533', 'm534', 'm535', 'm536', 'm537', 'm538', 'm539', 'm540', 'm541', 'm542', 'm543', 'm544', 'm545', 'm546', 'm547', 'm548', 'm549', 'm550', 'm551', 'm552', 'm553', 'm554', 'm555', 'm556', 'm557', 'm558', 'm559', 'm560', 'm561', 'm562', 'm563', 'm564', 'm565', 'm566', 'm567', 'm568', 'm569', 'm570', 'm571', 'm572', 'm573', 'm574', 'm575', 'm576', 'm577', 'm578', 'm579', 'm580', 'm581', 'm582', 'm583', 'm584', 'm585', 'm586', 'm587', 'm588', 'm589', 'm590', 'm591', 'm592', 'm593', 'm594', 'm595', 'm596', 'm597', 'm598', 'm599', 'm600', 
'm601', 'm602', 'm603', 'm604', 'm605', 'm606', 'm607', 'm608', 'm609', 'm610', 'm611', 'm612', 'm613', 'm614', 'm615', 'm616', 'm617', 'm618', 'm619', 'm620', 'm621', 'm622', 'm623', 'm624', 'm625', 'm626', 'm627', 'm628', 'm629', 'm630', 'm631', 'm632', 'm633', 'm634', 'm635', 'm636', 'm637', 'm638', 'm639', 'm640', 'm641', 'm642', 'm643', 'm644', 'm645', 'm646', 'm647', 'm648', 'm649', 'm650', 'm651', 'm652', 'm653', 'm654', 'm655', 'm656', 'm657', 'm658', 'm659', 'm660', 'm661', 'm662', 'm663', 'm664', 'm665', 'm666', 'm667', 'm668', 'm669', 'm670', 'm671', 'm672', 'm673', 'm674', 'm675', 'm676', 'm677', 'm678', 'm679', 'm680', 'm681', 'm682', 'm683', 'm684', 'm685', 'm686', 'm687', 'm688', 'm689', 'm690', 'm691', 'm692', 'm693', 'm694', 'm695', 'm696', 'm697', 'm698', 'm699', 'm700', 'm701', 'm702', 'm703', 'm704', 'm705', 'm706', 'm707', 'm708', 'm709', 'm710', 'm711', 'm712', 'm713', 'm714', 'm715', 'm716', 'm717', 'm718', 'm719', 'm720', 'm721', 'm722', 'm723', 'm724', 'm725', 'm726', 'm727', 'm728', 'm729', 'm730', 'm731', 'm732', 'm733', 'm734', 'm735', 'm736', 'm737', 'm738', 'm739', 'm740', 'm741', 'm742', 'm743', 'm744', 'm745', 'm746', 'm747', 'm748', 'm749', 'm750', 'm751', 'm752', 'm753', 'm754', 'm755', 'm756', 'm757', 'm758', 'm759', 'm760', 'm761', 'm762', 'm763', 'm764', 'm765', 'm766', 'm767', 'm768', 'm769', 'm770', 'm771', 'm772', 'm773', 'm774', 'm775', 'm776', 'm777', 'm778', 'm779', 'm780', 'm781', 'm782', 'm783', 'm784', 'm785', 'm786', 'm787', 'm788', 'm789', 'm790', 'm791', 'm792', 'm793', 'm794', 'm795', 'm796', 'm797', 'm798', 'm799', 'm800', 
'm801', 'm802', 'm803', 'm804', 'm805', 'm806', 'm807', 'm808', 'm809', 'm810', 'm811', 'm812', 'm813', 'm814', 'm815', 'm816', 'm817', 'm818', 'm819', 'm820', 'm821', 'm822', 'm823', 'm824', 'm825', 'm826', 'm827', 'm828', 'm829', 'm830', 'm831', 'm832', 'm833', 'm834', 'm835', 'm836', 'm837', 'm838', 'm839', 'm840', 'm841', 'm842', 'm843', 'm844', 'm845', 'm846', 'm847', 'm848', 'm849', 'm850', 'm851', 'm852', 'm853', 'm854', 'm855', 'm856', 'm857', 'm858', 'm859', 'm860', 'm861', 'm862', 'm863', 'm864', 'm865', 'm866', 'm867', 'm868', 'm869', 'm870', 'm871', 'm872', 'm873', 'm874', 'm875', 'm876', 'm877', 'm878', 'm879', 'm880', 'm881', 'm882', 'm883', 'm884', 'm885', 'm886', 'm887', 'm888', 'm889', 'm890', 'm891', 'm892', 'm893', 'm894', 'm895', 'm896', 'm897', 'm898', 'm899', 'm900', 'm901', 'm902', 'm903', 'm904', 'm905', 'm906', 'm907', 'm908', 'm909', 'm910', 'm911', 'm912', 'm913', 'm914', 'm915', 'm916', 'm917', 'm918', 'm919', 'm920', 'm921', 'm922', 'm923', 'm924', 'm925', 'm926', 'm927', 'm928', 'm929', 'm930', 'm931', 'm932', 'm933', 'm934', 'm935', 'm936', 'm937', 'm938', 'm939', 'm940', 'm941', 'm942', 'm943', 'm944', 'm945', 'm946', 'm947', 'm948', 'm949', 'm950', 'm951', 'm952', 'm953', 'm954', 'm955', 'm956', 'm957', 'm958', 'm959', 'm960', 'm961', 'm962', 'm963', 'm964', 'm965', 'm966', 'm967', 'm968', 'm969', 'm970', 'm971', 'm972', 'm973', 'm974', 'm975', 'm976', 'm977', 'm978', 'm979', 'm980', 'm981', 'm982', 'm983', 'm984', 'm985', 'm986', 'm987', 'm988', 'm989', 'm990', 'm991', 'm992', 'm993', 'm994', 'm995', 'm996', 'm997', 'm998', 'm999', 'm1000', 
'm1001', 'm1002', 'm1003', 'm1004', 'm1005', 'm1006', 'm1007', 'm1008', 'm1009', 'm1010', 'm1011', 'm1012', 'm1013', 'm1014', 'm1015', 'm1016', 'm1017', 'm1018', 'm1019', 'm1020']

# Create an input function reading a file using the Dataset API
# Then provide the results to the Estimator API


def my_input_fn(file_path, perform_shuffle=True, repeat_count=10):
    def decode_csv(line):
        parsed_line = tf.decode_csv(line,[

[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], 
[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], 
[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], 
[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], 
[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], 
[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0]
])
        label = parsed_line[-1]  # Last element is the label
        del parsed_line[-1]  # Delete last element
        features = parsed_line  # Everything but last elements are the features
        d = dict(zip(feature_names, features)), label
        return d

    dataset = (tf.data.TextLineDataset(file_path)  # Read text file
               .skip(1)  # Skip header row
               .map(decode_csv))  # Transform each elem by applying decode_csv fn
    if perform_shuffle:
        # Randomizes input using a window of 256 elements (read into memory)
        dataset = dataset.shuffle(buffer_size=256)
    dataset = dataset.repeat(repeat_count)  # Repeats dataset this # times
    dataset = dataset.batch(256)  # Batch size to use
    iterator = dataset.make_one_shot_iterator()
    batch_features, batch_labels = iterator.get_next()
    return batch_features, batch_labels

next_batch = my_input_fn(FILE_TRAIN, True)  # Will return 32 random elements

# Create the feature_columns, which specifies the input to our model
# All our input features are numeric, so use numeric_column for each one
feature_columns = [tf.feature_column.numeric_column(k) for k in feature_names]

# Create a deep neural network regression classifier
# Use the DNNClassifier pre-made estimator
classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,  # The input features to our model
    hidden_units=[1020,510,256,32],  # Two layers, each with 10 neurons
    n_classes=6,
    model_dir=PATH)  # Path to where checkpoints etc are stored

# Train our model, use the previously function my_input_fn
# Input to training is a file with training example
# Stop training after 8 iterations of train data (epochs)

#enter the values into this array
prediction_input = [ array of 1020 points ] 




def new_input_fn():
    def decode(x):
        x = tf.split(x, 1020)  # Need to split into our 4 features
        return dict(zip(feature_names, x))  # To build a dict of them

    dataset = tf.data.Dataset.from_tensor_slices(prediction_input)
    dataset = dataset.map(decode)
    iterator = dataset.make_one_shot_iterator()
    next_feature_batch = iterator.get_next()
    return next_feature_batch, None  # In prediction, we have no labels

# Predict all our prediction_input
predict_results = classifier.predict(input_fn=new_input_fn)



# Print results
print("Predictions:")
for idx, prediction in enumerate(predict_results):
    type = prediction["class_ids"][0]  # Get the predicted class (index)
    print("Output is")
    print(type)

