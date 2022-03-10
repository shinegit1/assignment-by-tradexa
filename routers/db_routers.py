class Products:
    apps={'products'}
    
    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.apps:
            return 'products_db'
        return None
    
    def sb_for_write(self,model,**hints):
        if model._meta.app_label in self.apps:
            return 'products_db'
        return None
    
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.apps:
            return db=='products_db'
        else:
            return False