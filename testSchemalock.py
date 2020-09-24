#For all of those combined prod/viewer environments, something to check for locks without refusing connections
def super_delete(feature_or_table):
    """This is an admin-level delete; checks for schema lock, disconnects if necessary, then proceeds to delete"""
    if not arcpy.TestSchemaLock(feature_or_table):
        arcpy.DisconnectUser(arcpy.env.workspace, 'ALL')
    arcpy.Delete_management(feature_or_table)

def super_rename(feature_or_table_original, feature_or_table_new):
    """This is an admin-level rename; checks for schema lock, disconnects if necessary, then proceeds to delete"""
    if not arcpy.TestSchemaLock(feature_or_table):
        arcpy.DisconnectUser(arcpy.env.workspace, 'ALL')
    arcpy.Rename_management(feature_or_table_original, feature_or_table_new)
