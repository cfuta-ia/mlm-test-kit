class Templates:
    """ """
    @staticmethod
    def createModel(modelType, algorithm, data):
        """ """
        return [
            {"element": {"elementType": "Button", "value": "create"}}
            , {"element": {"elementType": "TextField", "value": "name-entry"}}
            , {"element": {"elementType": "Button", "value": "next"}}
            , {"element": {"elementType": "Option", "value": modelType}}
            , {"element": {"elementType": "Option", "value": algorithm}}
            , {"element": {"elementType": "Button", "value": "next"}}
            , {"element": {"elementType": "Button", "value": "next"}}
            , {"element": {"elementType": "Button", "value": "csv"}}
            , {"element": {"elementType": "FileUpload", "data": data}}
            , {"element": {"elementType": "Button", "value": "load-data"}}
            , {"element": {"elementType": "Button", "value": "next"}}
            , {"element": {"elementType": "Button", "value": "next"}}
            , {"element": {"elementType": "Button", "value": "confirm-create"}}
        ]
    
    @classmethod
    def getTemplate(cls, name, **kwargs):
        """ """
        tmp = getattr(cls, name)
        return tmp(**kwargs)