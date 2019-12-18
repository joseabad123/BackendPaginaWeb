# Simple_jwt imports
# ...

# Rest framework imports
from rest_framework import permissions

# Local imports
from core.models import (Role,
                         User,
                         Person,
                         Person_Role)
from core import utils # Trae algunas funcionalidaddes utiles

class IsSuperadmin(permissions.BasePermission):
    """
    Clase que sirve para proteger las vistas
    Solo permite acceder a los usuarios con un rol asociado de superadmin
    """

    def has_permission(self, request, view):
        """
        Sobreescribimos este método para que verifique si el usuario que trata de acceder es superadmin o no
        Devuelve 'True' si es que si lo es y 'False', si no lo es
        """
        # ? Dando permisos a los GET
        if(request.method in permissions.SAFE_METHODS):
            return True


        superadmin_id = utils.get_role_id_by_name('superadmin')                 # Obtnemos el id del superadmin

        try:
            user_person_id = request.user.person_id.person_id           # Obtenemos el id de la persona asociada a la usuario
            respective_person_role = utils.get_person_role_by_id(person_id=user_person_id, role_id=superadmin_id)    # Obtenemos el person_role (Tabla de muchos a muchos)
        except:
            return False


        if(respective_person_role != None):
            if (respective_person_role.role_id.role_id == superadmin_id):
                # Si es superadmin devolvemos True
                return True
            else:
                # Si no lo es dedvolvemos False
                return False
        else:
            return False




class IsCoordinator(permissions.BasePermission):
    """
    Clase que sirve para dar permiso a vistas, cuando el token pertenezca a un usuario
    con el rol asociado 'coordidnador'
    """
    message = 'This user it is not a coordinator'
    def isCoordinator(self, user_person_id):


        coordinator_role_id = utils.get_role_id_by_name('coordinador')                 # Obtnemos el id del coordinator rol


        respective_person_role_id = utils.get_person_role_by_id(person_id=user_person_id, role_id=coordinator_role_id)    # Obtenemos el person_role (Tabla de muchos a muchos)


        if(respective_person_role_id != None):
            if (respective_person_role_id.role_id.role_id == coordinator_role_id):
                # Si es coordinadoor devolvemos True
                return True
            else:
                # Si no lo es devolvemos False
                return False
        else:
            return False


    def has_permission(self, request, view):
        """
        Sobreescribimos este método para que verifique si el usuario que trata de acceder es coordinador o no
        Devuelve 'True' si es que si lo es y 'False', si no lo es
        """
        return self.isCoordinator(user_person_id=request.user.person_id.person_id)






class IsRespectiveCoordinator(IsCoordinator):
    """
    Clase que sirve para dar permiso a vistas cuando el usuario sea cordinador y quiera accedere a contenido de una carrera específica
    con el rol asociado 'coordidnador'
    """
    message = 'This user it is not a coordinator or it is not the coordinator of this career'


    def has_permission(self, request, view):
        """
        Sobreescribimos este método para que verifique si el usuario que trata de acceder es coordinador o no
        Devuelve 'True' si es que si lo es y 'False', si no lo es
        """



        target_career_id = request.data.get('university_career_id')

        coordinator_role_id = utils.get_role_id_by_name('coordinador')

        respective_person_role_id = utils.get_person_role_by_id(person_id=request.user.person_id.person_id, role_id=coordinator_role_id)
        print(respective_person_role_id)
        if(respective_person_role_id != None):

            if (respective_person_role_id.role_id.role_id == coordinator_role_id):

                # Si es coordinadoor, verificamos que sea el mismo de la carrera
                career_id = int(respective_person_role_id.university_career_id.item_category_id)
                target_career_id = int(target_career_id)
                if(respective_person_role_id.university_career_id.item_category_id == target_career_id):

                    return True

            else:
                # Si no lo es devolvemos False

                return False
        else:

            return False

        return False

