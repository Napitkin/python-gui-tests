class GroupHelper:

    def __init__(self, app):
        self.delete_group = None
        self.group_editor = None
        self.app = app


    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list


    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def del_group(self, name):
        self.open_group_editor()
        # Находим дерево списка групп
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        # Корневой элемент дерева
        root = tree.tree_root()
        # Поиск нужной группы по имени
        target_node = None
        for i in root.children():
            if i.text() == name:
                target_node = i
                break
        # Если группа найдена, кликаем по ней
        if target_node is not None:
            target_node.click()
            self.open_group_delete()
        else:
            print(f"Группа с именем '{name}' не найдена.")


    def open_group_editor(self):
        self.app.main_window.window(auto_id = "groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")


    def open_group_delete(self):
        self.delete_group = self.app.application.window(title="Delete group")
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group.wait("visible")
        self.delete_group.window(auto_id="uxDeleteAllRadioButton").click()
        self.delete_group.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()


    def close_group_editor(self):
        self.group_editor.close()