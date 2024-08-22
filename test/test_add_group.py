def test_add_group(app):
     old_list = app.groups.get_group_list()
     app.groups.add_new_group("my group")
     new_list = app.groups.get_group_list()
     old_list.append("my group")
     assert sorted(old_list) == sorted(new_list)

def test_del_group(app):
     if len(app.groups.get_group_list()) is not "my group":
          app.groups.add_new_group("my group")
     old_list = app.groups.get_group_list()
     app.groups.del_group("my group")
     new_list = app.groups.get_group_list()
     old_list.remove("my group")
     assert sorted(old_list) == sorted(new_list)