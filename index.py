from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
# import MySQLdb
import mysql.connector
from PyQt5.uic import loadUiType
import datetime
from xlrd import *
from xlsxwriter import *
import re
from PyQt5 import QtGui, QtCore

ui, _ = loadUiType('main.ui')

login, _ = loadUiType('Intro.ui')
db_host = 'localhost'
db_user = 'sammy'
db_password = 'P@$$w0rd'
db = 'library_management_system'


class Login(QMainWindow, login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.pushButton_10.clicked.connect(self.Handel_Login)
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Handel_UI_Changes(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Login(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        username = self.lineEdit_6.text()
        password = self.lineEdit_7.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[2] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Entered Your Username And Password Correctly')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.QDark_Theme()

        self.Show_Author()
        self.Show_Category()
        self.Show_Publisher()

        self.Show_Category_Combobox()
        self.Show_Branch_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()
        self.Show_item_type_Combobox()
        self.Show_status_Combobox()

        self.Show_All_Clients()
        self.Show_All_Books()

        self.Show_All_Operations()
        self.Open_Books_Tab()

    def Handel_UI_Changes(self):
        # self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):
        self.pushButton_17.clicked.connect(self.Delete_Books)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_24.clicked.connect(self.Open_Books_Tab)
        self.pushButton_4.clicked.connect(self.Open_CLients_Tab)
        self.pushButton_3.clicked.connect(self.Open_Dashboard_Tab)
        self.pushButton_5.clicked.connect(self.Open_History_Tab)
        self.pushButton_7.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_63.clicked.connect(self.Add_New_Book)
        self.pushButton_9.clicked.connect(self.Search_Books_all_items)
        self.pushButton_12.clicked.connect(self.Search_Books)
        self.pushButton_16.clicked.connect(self.Edit_Books)
        self.pushButton_10.clicked.connect(self.Export_Books)

        self.pushButton_49.clicked.connect(self.Add_Branch)
        self.pushButton_53.clicked.connect(self.Add_Category)
        self.pushButton_51.clicked.connect(self.Add_Author)
        self.pushButton_50.clicked.connect(self.Add_Publisher)
        self.pushButton_80.clicked.connect(self.Export_All_Operations)

        # self.pushButton_11.clicked.connect(self.Add_New_User)
        # self.pushButton_12.clicked.connect(self.Login)
        self.pushButton_13.clicked.connect(self.all_operation_search)
        self.pushButton_44.clicked.connect(self.Retrieve_Today_search)

        self.pushButton_43.clicked.connect(self.Add_New_Client)
        self.pushButton_42.clicked.connect(self.Search_Client_all_clients)
        self.pushButton_47.clicked.connect(self.Search_Client)
        self.pushButton_46.clicked.connect(self.Edit_Client)
        self.pushButton_48.clicked.connect(self.Delete_Client)
        #
        # self.pushButton_6.clicked.connect(self.Handel_Day_Operations)
        self.pushButton_6.clicked.connect(self.Open_Reports_Tab)

        # self.pushButton_29.clicked.connect(self.Export_Day_Operations)
        # self.pushButton_27.clicked.connect(self.Export_Books)
        self.pushButton_78.clicked.connect(self.Export_Clients)

    # def Show_Themes(self):
    #     self.groupBox_3.show()
    #
    # def Hiding_Themes(self):
    #     self.groupBox_3.hide()

    ########################################
    ######### opening tabs #################
    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)
        self.Show_Today_Operations()

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.Show_Branch_Combobox()
        self.Show_Category_Combobox()
        self.Show_item_type_Combobox()
        self.Show_status_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()
        self.Show_lock_Combobox()
        self.Show_All_Books()
        self.set_date_Edit()
        self.Show_publication_year_Combobox()
        self.set_book_fields_delete()

    def Open_CLients_Tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)
        self.Show_search_client_Combobox()
        self.set_edit_client_fields()
        self.Show_All_Clients()

    def Open_Dashboard_Tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.Show_Retrieve_Today()
        self.Show_search_dashboard_Combobox()

    def Open_History_Tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.Show_All_Operations()
        self.Show_Branch_Combobox()

    def Open_Reports_Tab(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(6)

    ########################################
    ######### Day Operations #################
    def Handel_Day_Operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_29.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        print(today_date)
        print(to_date)

        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute('''
            INSERT INTO dayoperations(book_name, client, type , days , date , to_date )
            VALUES (%s , %s , %s, %s , %s , %s)
        ''', (book_title, client_name, type, days_number, today_date, to_date))

        self.db.commit()
        self.statusBar().showMessage('New Operation Added')

        self.Show_All_Operations()

    def Show_Today_Operations(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        self.cur.execute(''' 
            SELECT c.name as client,b.type as book_type , b.name as book , b.code  , br.name as branch , d.date_from , d.date_to ,d.retrieve_date , DATEDIFF(CURRENT_DATE,d.date_to) as delay,DATEDIFF(CURRENT_DATE,d.date_to) * b.price as fees FROM dayoperations d 
            INNER JOIN clients c ON c.id = d.client_id
            INNER JOIN book b ON b.id = d.book_id
            INNER JOIN branch br ON br.id = d.branch_id
            WHERE d.retrieve_date IS NULL
            AND d.date_to < CURRENT_DATE
            AND DATE(d.create_date) = CURRENT_DATE;
        ''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.cur.execute(''' 
                    SELECT c.name as client ,b.type as book_type, b.name as book , b.code  , br.name as branch , d.date_from , d.date_to ,d.retrieve_date , d.delay,d.fees FROM dayoperations d 
                    INNER JOIN clients c ON c.id = d.client_id
                    INNER JOIN book b ON b.id = d.book_id
                    INNER JOIN branch br ON br.id = d.branch_id
                    WHERE d.retrieve_date IS NULL
                    AND d.date_to >= CURRENT_DATE
                    AND DATE(d.create_date) = CURRENT_DATE;

                ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.cur.execute(''' 
                            SELECT c.name as client ,b.type as book_type, b.name as book , b.code , br.name as branch , d.date_from , d.date_to ,d.retrieve_date , d.delay,d.fees FROM dayoperations d 
                            INNER JOIN clients c ON c.id = d.client_id
                            INNER JOIN book b ON b.id = d.book_id
                            INNER JOIN branch br ON br.id = d.branch_id
                            WHERE d.retrieve_date IS NOT NULL
                            AND DATE(d.create_date) = CURRENT_DATE;
                        ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def all_operation_search(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        client_data = self.lineEdit_8.text()
        branch = self.comboBox_14.currentText()
        self.cur.execute(''' 
                            SELECT c.name as client , br.name as branch , d.date_from ,b.type as book_type , b.code , b.name as book ,d.retrieve_date FROM dayoperations d 
                            INNER JOIN clients c ON c.id = d.client_id
                            INNER JOIN book b ON b.id = d.book_id
                            INNER JOIN branch br ON br.id = d.branch_id
                            WHERE d.retrieve_date IS NULL
                            AND d.date_to < CURRENT_DATE;
                        ''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        for row, form in enumerate(data):
            if client_data or branch:
                if client_data and branch:
                    if form[0] == client_data and form[1] == branch:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                elif client_data:
                    if form[0] == client_data:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                elif branch:
                    if form[1] == branch:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)

        self.cur.execute(''' 
                            SELECT c.name as client , br.name as branch , d.date_from ,b.type as book_type , b.code , b.name as book ,d.retrieve_date FROM dayoperations d 
                                    INNER JOIN clients c ON c.id = d.client_id
                                    INNER JOIN book b ON b.id = d.book_id
                                    INNER JOIN branch br ON br.id = d.branch_id
                                    WHERE d.retrieve_date IS NULL
                                    AND d.date_to >= CURRENT_DATE;

                                ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            if client_data or branch:
                if client_data and branch:
                    if form[0] == client_data and form[1] == branch:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                elif client_data:
                    if form[0] == client_data:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                elif branch:
                    if form[1] == branch:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)

        self.cur.execute(''' 
                            SELECT c.name as client , br.name as branch , d.date_from ,b.type as book_type , b.code , b.name as book ,d.retrieve_date FROM dayoperations d 
                                            INNER JOIN clients c ON c.id = d.client_id
                                            INNER JOIN book b ON b.id = d.book_id
                                            INNER JOIN branch br ON br.id = d.branch_id
                                            WHERE d.retrieve_date IS NOT NULL;
                                        ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            if client_data or branch:
                if client_data and branch:
                    if form[0] == client_data and form[1] == branch:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                elif client_data:
                    if form[0] == client_data:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                elif branch:
                    if form[1] == branch:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_2.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)

    def Show_All_Operations(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        self.cur.execute(''' 
                    SELECT c.name as client , br.name as branch , d.date_from ,b.type as book_type , b.code , b.name as book ,d.retrieve_date FROM dayoperations d 
                    INNER JOIN clients c ON c.id = d.client_id
                    INNER JOIN book b ON b.id = d.book_id
                    INNER JOIN branch br ON br.id = d.branch_id
                    WHERE d.retrieve_date IS NULL
                    AND d.date_to < CURRENT_DATE;
                ''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget_2.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

        self.cur.execute(''' 
                    SELECT c.name as client , br.name as branch , d.date_from ,b.type as book_type , b.code , b.name as book ,d.retrieve_date FROM dayoperations d 
                            INNER JOIN clients c ON c.id = d.client_id
                            INNER JOIN book b ON b.id = d.book_id
                            INNER JOIN branch br ON br.id = d.branch_id
                            WHERE d.retrieve_date IS NULL
                            AND d.date_to >= CURRENT_DATE;

                        ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget_2.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

        self.cur.execute(''' 
                    SELECT c.name as client , br.name as branch , d.date_from ,b.type as book_type , b.code , b.name as book ,d.retrieve_date FROM dayoperations d 
                                    INNER JOIN clients c ON c.id = d.client_id
                                    INNER JOIN book b ON b.id = d.book_id
                                    INNER JOIN branch br ON br.id = d.branch_id
                                    WHERE d.retrieve_date IS NOT NULL;
                                ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget_2.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

    def Retrieve_Today_search(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        search_data = self.lineEdit_73.text()
        comboBox = self.comboBox_62.currentText()
        index = self.comboBox_62.findText(comboBox)

        self.cur.execute(''' 
                            SELECT c.name as client  ,b.type as book_type , b.code, b.name as book  , br.name as branch , d.date_from , d.date_to ,d.retrieve_date , d.delay,d.fees FROM dayoperations d 
                            INNER JOIN clients c ON c.id = d.client_id
                            INNER JOIN book b ON b.id = d.book_id
                            INNER JOIN branch br ON br.id = d.branch_id
                            WHERE d.retrieve_date IS NULL
                            AND d.date_to <= CURRENT_DATE;
                        ''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        for row, form in enumerate(data):
            if search_data:
                if index == 0:
                    if form[0] == search_data:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_3.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                elif index == 1:
                    if str(form[5]) == search_data:
                        for column, item in enumerate(form):
                            item = QTableWidgetItem(str(item))
                            item.setTextAlignment(Qt.AlignHCenter)
                            self.tableWidget_3.setItem(row, column, item)
                            column += 1

                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)

            else:
                for column, item in enumerate(form):
                    item = QTableWidgetItem(str(item))
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.tableWidget_3.setItem(row, column, item)
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Show_Retrieve_Today(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        self.cur.execute(''' 
                    SELECT c.name as client  ,b.type as book_type , b.code, b.name as book  , br.name as branch , d.date_from , d.date_to ,d.retrieve_date , d.delay,d.fees FROM dayoperations d 
                    INNER JOIN clients c ON c.id = d.client_id
                    INNER JOIN book b ON b.id = d.book_id
                    INNER JOIN branch br ON br.id = d.branch_id
                    WHERE d.retrieve_date IS NULL
                    AND d.date_to <= CURRENT_DATE;
                ''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget_3.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)

    ########################################
    ######### Books #################

    def Show_All_Books(self, data=[]):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        search_pattern = 'type,code,name,category_id,branch_id,physical_position,price,status,check_out,author_id,publisher_id,publication_year,part_order,added_date,description'
        sql = "SELECT %s FROM book" % search_pattern
        self.cur.execute(sql)
        if not data:
            data = self.cur.fetchall()

        self.tableWidget_22.setRowCount(0)
        self.tableWidget_22.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                if column == 3:
                    item = self.get_name_by_id('category', item)
                if column == 4:
                    item = self.get_name_by_id('branch', item)
                if column == 9:
                    item = self.get_name_by_id('authors', item)
                if column == 10:
                    item = self.get_name_by_id('publisher', item)
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget_22.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget_22.rowCount()
            self.tableWidget_22.insertRow(row_position)

        self.db.close()

    def get_all_required_column(self, table):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        self.cur.execute('''select tab.table_schema as database_name,
    tab.table_name,
    col.ordinal_position as column_id,
    col.column_name,
    col.data_type,
    case when col.numeric_precision is not null
            then col.numeric_precision
        else col.character_maximum_length end as max_length,
    case when col.datetime_precision is not null
            then col.datetime_precision
        when col.numeric_scale is not null
            then col.numeric_scale
        else 0 end as 'precision'
from information_schema.tables as tab
join information_schema.columns as col
        on col.table_schema = tab.table_schema
        and col.table_name = tab.table_name
        and col.is_nullable = 'no'
where tab.table_schema not in ('information_schema', 'sys', 
                               'mysql','performance_schema')
      and tab.table_type = 'BASE TABLE'  
      and tab.table_schema = %s
      and tab.table_name = %s
order by tab.table_schema,
         tab.table_name,
         col.ordinal_position;
''', (db, table))
        data = self.cur.fetchall()
        self.db.commit()
        return data

    def search_by_name(self, table, name):
        query = "SELECT id,name FROM %s WHERE name = '%s' ;" % (table, name)
        self.cur.execute(query)
        data = self.cur.fetchall()
        return data[0][0]

    def get_name_by_id(self, table, id):
        query = "SELECT name,id FROM %s WHERE id = %s ;" % (table, id)
        self.cur.execute(query)
        data = self.cur.fetchall()
        return data[0][0]

    def set_date_Edit(self):
        self.dateEdit_6.setDate(QtCore.QDate.currentDate())
        self.dateEdit_6.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dateEdit_6.setCalendarPopup(True)

    def check_code(self, code):
        query = "SELECT name,id FROM book WHERE code = '%s' ;" % (code)
        self.cur.execute(query)
        data = self.cur.fetchone()
        return False if not data else True

    def combo_set_value(self, combo, text):
        print(text)
        AllItems = [combo.itemText(i) for i in range(combo.count())]
        index = combo.findData(text)
        print(index)
        if index >= 0:
            combo.setCurrentIndex(index)

    def Add_New_Book(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            name = self.lineEdit_3.text()
            description = self.textEdit.toPlainText()
            code = self.lineEdit_10.text()
            category_id = self.comboBox_40.currentText()
            type = self.comboBox_5.currentText()
            branch_id = self.comboBox_41.currentText()
            author_id = self.comboBox_50.currentText()
            publisher_id = self.comboBox_51.currentText()
            status = self.comboBox_43.currentText()
            check_out = self.comboBox_45.currentText()
            price = self.lineEdit_11.text()
            physical_position = self.lineEdit_12.text()
            publication_year = self.lineEdit_16.text()
            part_order = self.spinBox.value()
            added_date = self.dateEdit_6.date().toPyDate()
            if not price:
                price = 0
            else:
                if not str(price).isdigit():
                    self.statusBar().showMessage('Price Must Be A Number')
                    return True
            if publication_year:
                if not str(publication_year).isdigit():
                    self.statusBar().showMessage('Publication Year Must Be A Number')
                    return True
            data = self.get_all_required_column('book')
            result = list(map(lambda x: x[3], data))
            for res in result:
                if res != 'id':
                    if not eval(res):
                        self.statusBar().showMessage('%s is required' % res)
                        return True
            category_id = self.search_by_name('category', category_id)
            branch_id = self.search_by_name('branch', branch_id)
            author_id = self.search_by_name('authors', author_id)
            publisher_id = self.search_by_name('publisher', publisher_id)
            self.cur.execute('''
                INSERT INTO book(name,description,code,category_id,type,branch_id,author_id,publisher_id,status,check_out,price,physical_position,publication_year,part_order,added_date)
                VALUES (%s , %s , %s , %s , %s , %s , %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                name, description, code, category_id, type, branch_id, author_id, publisher_id, status, check_out,
                price,
                physical_position, publication_year, part_order, added_date))

            self.db.commit()
            self.statusBar().showMessage('New Book Added')

            self.lineEdit_3.setText('')
            self.lineEdit_10.setText('')
            self.lineEdit_11.setText('')
            self.lineEdit_12.setText('')
            self.lineEdit_16.setText('')
            self.textEdit.setPlainText('')
            self.comboBox_40.setCurrentIndex(0)
            self.comboBox_5.setCurrentIndex(0)
            self.comboBox_41.setCurrentIndex(0)
            self.comboBox_50.setCurrentIndex(0)
            self.comboBox_51.setCurrentIndex(0)
            self.comboBox_43.setCurrentIndex(0)
            self.comboBox_45.setCurrentIndex(0)
            self.spinBox.setValue(1)
            self.set_date_Edit()
            self.Show_All_Books()
            self.Open_Books_Tab()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Search_Books(self):

        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        code = self.lineEdit_13.text()
        search_pattern = "type,code,name,category_id,branch_id,physical_position,price,status,check_out,author_id,publisher_id,publication_year,part_order,added_date,description"
        sql = ''' SELECT %s FROM book WHERE code = '%s' ''' % (search_pattern, code)
        self.cur.execute(sql)

        data = self.cur.fetchone()

        print(data)
        if data:
            self.lineEdit_5.setText(str(data[2]))
            self.textEdit_2.setPlainText(data[-1])
            self.lineEdit_19.setText(str(data[5]))
            self.lineEdit_9.setText(str(data[6]))
            self.lineEdit_39.setText(str(data[11]))
            self.comboBox_4.setCurrentText(str(data[0]))
            self.comboBox_9.setCurrentText(str(data[7]))
            self.comboBox_17.setCurrentText(str(data[8]))
            self.comboBox_8.setCurrentText(self.get_name_by_id('category', data[3]))
            self.comboBox_44.setCurrentText(self.get_name_by_id('branch', data[4]))
            self.comboBox_12.setCurrentText(self.get_name_by_id('authors', data[9]))
            self.comboBox_13.setCurrentText(self.get_name_by_id('publisher', data[10]))
            self.spinBox_2.setValue(data[12])
            self.dateEdit_7.setDate(QtCore.QDate(data[13].year, data[13].month, data[13].day))
        else:
            self.lineEdit_5.setText('')
            self.textEdit_2.setPlainText('')
            self.lineEdit_19.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_39.setText('')
            self.spinBox_2.setValue(1)
            self.dateEdit_7.setDate(QtCore.QDate.currentDate())

    def set_book_fields_delete(self):
        self.lineEdit_5.setText('')
        self.textEdit_2.setPlainText('')
        self.lineEdit_19.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_39.setText('')
        self.spinBox_2.setValue(1)
        self.dateEdit_7.setDate(QtCore.QDate.currentDate())

    def Search_Books_all_items(self):

        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        search_pattern = "type,code,name,category_id,branch_id,physical_position,price,status,check_out,author_id,publisher_id,publication_year,part_order,added_date,description"
        book_title = self.lineEdit_2.text()
        item_type = self.comboBox_3.currentText()
        if re.match(r"---.+---", item_type):
            item_type = False
        category_id = self.comboBox_2.currentText()
        if re.match(r"---.+---", category_id):
            category_id = False

        publication_year = self.comboBox_7.currentText()
        if re.match(r"---.+---", publication_year):
            publication_year = False

        author_id = self.comboBox_6.currentText()
        if re.match(r"---.+---", author_id):
            author_id = False
        sql = ""
        if book_title:
            sql = " SELECT %s FROM book WHERE name = '%s' " % (search_pattern, book_title)
            if item_type:
                sql += "and type = '%s' " % (item_type)
            if category_id:
                category_id = self.search_by_name('category', category_id)
                sql += "and category_id = %s " % category_id
            if author_id:
                author_id = self.search_by_name('authors', author_id)
                sql += "and author_id = %s " % author_id
            if publication_year:
                sql += "and publication_year = '%s' " % publication_year
        elif item_type:
            sql = "SELECT %s FROM book WHERE type = '%s' " % (search_pattern, item_type)
            if category_id:
                category_id = self.search_by_name('category', category_id)
                sql += "and category_id = %s " % category_id
            if author_id:
                author_id = self.search_by_name('authors', author_id)
                sql += "and author_id = %s " % author_id
            if publication_year:
                sql += "and publication_year = '%s' " % publication_year

        elif category_id:
            category_id = self.search_by_name('category', category_id)
            sql = "SELECT %s FROM book WHERE category_id = %s " % (search_pattern, category_id)
            if author_id:
                author_id = self.search_by_name('authors', author_id)
                sql += "and author_id = %s " % author_id
            if publication_year:
                sql += "and publication_year = '%s' " % publication_year
        elif author_id:
            author_id = self.search_by_name('authors', author_id)
            sql = "SELECT %s FROM book WHERE author_id = %s " % (search_pattern, author_id)
            if publication_year:
                sql += "and publication_year = '%s' " % publication_year
        elif publication_year:
            sql = "SELECT %s FROM book WHERE publication_year = '%s' " % (search_pattern, publication_year)
        print(sql)
        if sql:
            self.cur.execute(sql)

            data = self.cur.fetchall()
            if data:
                self.Show_All_Books(data)
            else:
                self.tableWidget_22.setRowCount(0)
                self.tableWidget_22.insertRow(0)
        else:
            self.Show_All_Books()

    def Edit_Books(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        name = self.lineEdit_5.text()
        description = self.textEdit_2.toPlainText()
        code = self.lineEdit_13.text()
        category_id = self.comboBox_8.currentText()
        type = self.comboBox_4.currentText()
        branch_id = self.comboBox_44.currentText()
        author_id = self.comboBox_12.currentText()
        publisher_id = self.comboBox_13.currentText()
        status = self.comboBox_9.currentText()
        check_out = self.comboBox_17.currentText()
        price = self.lineEdit_9.text()
        physical_position = self.lineEdit_19.text()
        publication_year = self.lineEdit_39.text()
        part_order = self.spinBox_2.value()
        added_date = self.dateEdit_7.date().toPyDate()
        if not price:
            price = 0
        else:
            if not str(price).isdigit():
                self.statusBar().showMessage('Price Must Be A Number')
                return True
        if publication_year:
            if not str(publication_year).isdigit():
                self.statusBar().showMessage('Publication Year Must Be A Number')
                return True

        data = self.get_all_required_column('book')
        result = list(map(lambda x: x[3], data))
        for res in result:
            if res != 'id':
                if not eval(res):
                    self.statusBar().showMessage('%s is required' % res)
                    return True
        category_id = self.search_by_name('category', category_id)
        branch_id = self.search_by_name('branch', branch_id)
        author_id = self.search_by_name('authors', author_id)
        publisher_id = self.search_by_name('publisher', publisher_id)
        self.cur.execute('''
                UPDATE book SET name=%s ,description =%s ,category_id=%s,type=%s,branch_id=%s,author_id=%s,publisher_id=%s,status=%s,check_out=%s,price=%s,physical_position=%s,publication_year=%s,part_order=%s,added_date=%s WHERE code = %s
                ''', (
            name, description, category_id, type, branch_id, author_id, publisher_id, status, check_out, price,
            physical_position, publication_year, part_order, added_date, code))

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.Show_All_Books()

    def Delete_Books(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        code = self.lineEdit_13.text()

        warning = QMessageBox.warning(self, 'Delete Book', "are you sure you want to delete this book",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM book WHERE code = %s '''
            self.cur.execute(sql, [(code)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.Show_All_Books()
            self.Open_Books_Tab()

    ########################################
    ######### Clients #################
    def Show_All_Clients(self, data=[]):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        seacch_pattern = 'name , email,phone ,national_id,join_date'
        sql = ''' SELECT %s  FROM clients ''' % seacch_pattern
        self.cur.execute(sql)
        if not data:
            data = self.cur.fetchall()

        print(data)
        self.tableWidget_15.setRowCount(0)
        self.tableWidget_15.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget_15.setItem(row, column, item)
                column += 1

            row_position = self.tableWidget_15.rowCount()
            self.tableWidget_15.insertRow(row_position)

        self.db.close()

    def Add_New_Client(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            name = self.lineEdit_124.text()
            email = self.lineEdit_125.text()
            phone = self.lineEdit_138.text()
            national_id = self.lineEdit_139.text()
            join_date = datetime.date.today()

            if phone:
                if not str(phone).isdigit():
                    self.statusBar().showMessage('Phone Must Be A Numbers Only')
                    return True
            if national_id:
                if not str(national_id).isdigit():
                    self.statusBar().showMessage('National Id Must Be A Numbers Only')
                    return True
                if len(national_id) != 14:
                    self.statusBar().showMessage('National Id Must Be A 14 Numbers')
                    return True
            data = self.get_all_required_column('clients')
            result = list(map(lambda x: x[3], data))
            for res in result:
                if res != 'id':
                    if not eval(res):
                        self.statusBar().showMessage('%s is required' % res)
                        return True

            self.cur.execute('''
                INSERT INTO clients(name ,email,phone , national_id,join_date)
                VALUES (%s , %s,%s , %s,%s)
            ''', (name, email, phone, national_id, join_date))
            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('New Client Added')
            self.Show_All_Clients()

            self.lineEdit_124.setText('')
            self.lineEdit_125.setText('')
            self.lineEdit_138.setText('')
            self.lineEdit_139.setText('')
            self.Open_CLients_Tab()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Search_Client_all_clients(self):
        client_data = self.lineEdit_72.text()
        search_type = self.comboBox_61.currentText()
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        search_pattern = 'name,email,phone,national_id,join_date'
        if client_data and search_type:
            sql = ''' SELECT %s FROM clients WHERE %s = '%s' ''' % (search_pattern, search_type, client_data)

            self.cur.execute(sql)
            data = self.cur.fetchall()
            print(data)
            if data:
                self.Show_All_Clients(data)
            else:
                self.tableWidget_15.setRowCount(0)
                self.tableWidget_15.insertRow(0)
        else:
            self.Show_All_Clients()

    def Search_Client(self):
        client_data = self.lineEdit_86.text()
        search_type = self.comboBox_60.currentText()
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        search_pattern = 'name,email,phone,national_id,join_date'
        if client_data and search_type:
            sql = ''' SELECT %s FROM clients WHERE %s = '%s' ''' % (search_pattern, search_type, client_data)
            self.cur.execute(sql)
            data = self.cur.fetchone()
            print(data)
            if data:
                self.lineEdit_85.setText(data[0])
                self.lineEdit_83.setText(data[1])
                self.lineEdit_84.setText(data[2])
                self.lineEdit_82.setText(data[3])
            else:
                self.lineEdit_85.setText('')
                self.lineEdit_83.setText('')
                self.lineEdit_84.setText('')
                self.lineEdit_82.setText('')
        else:
            self.lineEdit_85.setText('')
            self.lineEdit_83.setText('')
            self.lineEdit_84.setText('')
            self.lineEdit_82.setText('')

    def set_edit_client_fields(self):
        self.lineEdit_86.setText('')
        self.lineEdit_85.setText('')
        self.lineEdit_83.setText('')
        self.lineEdit_84.setText('')
        self.lineEdit_82.setText('')

    def Edit_Client(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            name = self.lineEdit_85.text()
            email = self.lineEdit_83.text()
            phone = self.lineEdit_84.text()
            national_id = self.lineEdit_82.text()
            client_data = self.lineEdit_86.text()
            search_type = self.comboBox_60.currentText()

            if phone:
                if not str(phone).isdigit():
                    self.statusBar().showMessage('Phone Must Be A Numbers Only')
                    return True
            if national_id:
                if not str(national_id).isdigit():
                    self.statusBar().showMessage('National Id Must Be A Numbers Only')
                    return True
                if len(national_id) != 14:
                    self.statusBar().showMessage('National Id Must Be A 14 Numbers')
                    return True

            data = self.get_all_required_column('clients')
            result = list(map(lambda x: x[3], data))
            for res in result:
                if res != 'id':
                    if not eval(res):
                        self.statusBar().showMessage('%s is required' % res)
                        return True

            if search_type and client_data:
                sql = '''
                    UPDATE clients SET name = '%s' , email = '%s' ,phone = '%s', national_id = '%s' WHERE %s = '%s'
                ''' % (name, email, phone, national_id, search_type, client_data)
                self.cur.execute(sql)
                self.db.commit()
                self.db.close()
                self.statusBar().showMessage('Client Data Updated ')
                self.Show_All_Clients()
                self.set_edit_client_fields()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Delete_Client(self):
        warning_message = QMessageBox.warning(self, "Delete Clent", "are you sure you want to delete this client",
                                              QMessageBox.Yes | QMessageBox.No)

        if warning_message == QMessageBox.Yes:
            client_data = self.lineEdit_86.text()
            search_type = self.comboBox_60.currentText()
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            sql = ''' DELETE FROM clients WHERE %s = '%s' ''' % (search_type, client_data)
            self.cur.execute(sql)

            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('Client Deleted ')
            self.Show_All_Clients()
            self.set_edit_client_fields()

    ########################################
    ######### users #################

    def Add_New_User(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()

        if password == password2:
            self.cur.execute(''' 
                INSERT INTO users(user_name , user_email , user_password)
                VALUES (%s , %s , %s)
            ''', (username, email, password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_30.setText('please add a valid password twice')

    def Login(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        username = self.lineEdit_14.text()
        password = self.lineEdit_13.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('user match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_17.setText(row[1])
                self.lineEdit_15.setText(row[2])
                self.lineEdit_16.setText(row[3])

    def Edit_User(self):

        username = self.lineEdit_17.text()
        email = self.lineEdit_15.text()
        password = self.lineEdit_16.text()
        password2 = self.lineEdit_18.text()

        original_name = self.lineEdit_14.text()

        if password == password2:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            print(username)
            print(email)
            print(password)

            self.cur.execute('''
                UPDATE users SET user_name=%s , user_email=%s , user_password=%s WHERE user_name=%s
            ''', (username, email, password, original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            print('make sure you entered you password correctly')

    ########################################
    ######### settings #################

    def Add_Branch(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            name = self.lineEdit_87.text()

            self.cur.execute('''
                INSERT INTO branch (name) VALUES (%s)
            ''', (name,))
            self.db.commit()
            self.statusBar().showMessage('New Branch Added ')
            self.lineEdit_87.setText('')
            # self.Show_Category()
            self.Show_Branch_Combobox()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Add_Category(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            category_name = self.lineEdit_96.text()

            self.cur.execute('''
                INSERT INTO category (name) VALUES (%s)
            ''', (category_name,))
            self.db.commit()
            self.statusBar().showMessage('New Category Added ')
            self.lineEdit_96.setText('')
            # self.Show_Category()
            self.Show_Category_Combobox()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Show_Category(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM category''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def Add_Author(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            author_name = self.lineEdit_92.text()
            self.cur.execute('''
                INSERT INTO authors (name) VALUES (%s)
            ''', (author_name,))
            self.db.commit()
            self.lineEdit_92.setText('')
            self.statusBar().showMessage('New Author Added ')
            # self.Show_Author()
            self.Show_Author_Combobox()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Show_Author(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM authors''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Add_Publisher(self):
        try:
            self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
            self.cur = self.db.cursor(buffered=True)

            publisher_name = self.lineEdit_90.text()
            self.cur.execute('''
                INSERT INTO publisher (name) VALUES (%s)
            ''', (publisher_name,))

            self.db.commit()
            self.lineEdit_90.setText('')
            self.statusBar().showMessage('New Publisher Added ')
            # self.Show_Publisher()
            self.Show_Publisher_Combobox()
        except Exception as e:
            self.statusBar().showMessage(str(e))

    def Show_Publisher(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM publisher''')
        data = self.cur.fetchall()

        # if data:
        #     self.tableWidget_4.setRowCount(0)
        #     self.tableWidget_4.insertRow(0)
        #     for row, form in enumerate(data):
        #         for column, item in enumerate(form):
        #             self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
        #             column += 1
        #
        #         row_position = self.tableWidget_4.rowCount()
        #         self.tableWidget_4.insertRow(row_position)

    ########################################
    ######### show settings data in UI #################

    def Show_Category_Combobox(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM category ''')
        data = self.cur.fetchall()

        self.comboBox_40.clear()
        self.comboBox_8.clear()
        self.comboBox_2.clear()
        self.comboBox_2.addItem("---Category---")
        for category in data:
            self.comboBox_40.addItem(category[0])
            self.comboBox_2.addItem(category[0])
            self.comboBox_8.addItem(category[0])

    def Show_Branch_Combobox(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM branch ''')
        data = self.cur.fetchall()

        self.comboBox_41.clear()
        self.comboBox_44.clear()
        self.comboBox_14.clear()
        for branch in data:
            self.comboBox_41.addItem(branch[0])
            self.comboBox_44.addItem(branch[0])
            self.comboBox_14.addItem(branch[0])

    def Show_lock_Combobox(self):
        data = ['Can Be Rented', "In Library Only"]

        self.comboBox_45.clear()
        self.comboBox_17.clear()
        for item in data:
            self.comboBox_45.addItem(item)
            self.comboBox_17.addItem(item)

    def Show_search_client_Combobox(self):
        data = ['name', 'email', 'phone', 'national_id']

        self.comboBox_61.clear()
        self.comboBox_60.clear()
        for item in data:
            self.comboBox_61.addItem(item)
            self.comboBox_60.addItem(item)

    def Show_search_dashboard_Combobox(self):
        data = ['Client Name', 'Date Of Rent']

        self.comboBox_62.clear()
        for item in data:
            self.comboBox_62.addItem(item)

    def Show_Author_Combobox(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM authors''')
        data = self.cur.fetchall()

        self.comboBox_50.clear()
        self.comboBox_12.clear()
        self.comboBox_6.clear()
        self.comboBox_6.addItem("---Author---")
        for author in data:
            self.comboBox_50.addItem(author[0])
            self.comboBox_6.addItem(author[0])
            self.comboBox_12.addItem(author[0])

    def Show_publication_year_Combobox(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT DISTINCT publication_year FROM book''')
        data = self.cur.fetchall()

        self.comboBox_7.clear()
        self.comboBox_7.addItem("---Publication Year---")
        for item in data:
            self.comboBox_7.addItem(item[0])

    def Show_item_type_Combobox(self):
        data = ["Book", "Magazine", "Audio Material"]

        self.comboBox_5.clear()
        self.comboBox_4.clear()
        self.comboBox_3.clear()
        self.comboBox_3.addItem("---Item Type---")
        for type in data:
            self.comboBox_5.addItem(type)
            self.comboBox_3.addItem(type)
            self.comboBox_4.addItem(type)

    def Show_status_Combobox(self):
        data = ["New", "Old"]

        self.comboBox_43.clear()
        self.comboBox_9.clear()
        for type in data:
            self.comboBox_43.addItem(type)
            self.comboBox_9.addItem(type)

    def Show_Publisher_Combobox(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        self.cur.execute(''' SELECT name FROM publisher''')
        data = self.cur.fetchall()

        self.comboBox_51.clear()
        self.comboBox_13.clear()
        for publisher in data:
            self.comboBox_51.addItem(publisher[0])
            self.comboBox_13.addItem(publisher[0])

    ########################################
    ######### Export Data #################
    def Export_All_Operations(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)
        search_pattern = 'client , branch , date_from ,book_type , book_code,book_name, retrieve_date'
        headers = search_pattern.split(',')
        wb = Workbook('all_operations.xlsx')
        sheet1 = wb.add_worksheet()
        data = self.iterate(self.tableWidget_2)
        row = 0
        col = 0
        for header in headers:
            sheet1.write(row, col, header)
            col += 1

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')

    def iterate(self, table):
        list = []
        column = 0
        # rowCount() This property holds the number of rows in the table
        for row in range(table.rowCount() - 1):
            data = []
            for column in range(table.columnCount()):
                # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
                _item = table.item(row, column)
                if _item:
                    item = table.item(row, column).text()
                    data.append(item)
                else:
                    data.append('')
            if data:
                list.append(data)
        return list

    def Export_Books(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        search_pattern = 'type,code,name,category_id,branch_id,physical_position,price,status,check_out,author_id,publisher_id,publication_year,part_order,added_date,description'
        headers = search_pattern.split(',')
        sql = "SELECT %s FROM book" % search_pattern
        self.cur.execute(sql)
        data = self.cur.fetchall()

        data = self.iterate(self.tableWidget_22)

        wb = Workbook('all_books.xlsx')
        sheet1 = wb.add_worksheet()
        row = 0
        col = 0
        for header in headers:
            sheet1.write(row, col, header)
            col += 1

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Book Report Created Successfully')

    def Export_Clients(self):
        self.db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, db=db)
        self.cur = self.db.cursor(buffered=True)

        wb = Workbook('all_CLients.xlsx')
        sheet1 = wb.add_worksheet()

        search_pattern = 'name,email,phone,national_id,join_date'
        headers = search_pattern.split(',')

        data = self.iterate(self.tableWidget_15)
        row = 0
        col = 0
        for header in headers:
            sheet1.write(row, col, header)
            col += 1

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Clients Report Created Successfully')

    ########################################
    #########  UI Themes #################

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    cnx = mysql.connector.connect(user='root',
                                  password='Password123#@!',
                                  host=db_host)
    cursor = cnx.cursor(buffered=True)


    def executeScriptsFromFile(filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                if command.strip() != '':
                    cursor.execute(command)
            except IOError as msg:
                print("Command skipped: ", msg)


    executeScriptsFromFile(
        '/home/mohamed/library_management_system/Build-Library-Management-System-Python-PyQt5/db2.sql')
    cnx.commit()
    cursor.close()
    cnx.close()
    cnx = mysql.connector.connect(user=db_user,
                                  password=db_password,
                                  host=db_host, db=db)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SHOW TABLES;")
    data = cursor.fetchall()
    create_tables = True
    for item in data:
        if item[0] == 'users':
            create_tables = False
    if create_tables:
        executeScriptsFromFile(
            '/home/mohamed/library_management_system/Build-Library-Management-System-Python-PyQt5/db.sql')
        cnx.commit()
        cursor.close()
        cnx.close()
    main()
