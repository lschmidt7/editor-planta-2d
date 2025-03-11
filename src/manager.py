# from typing import List

# from src.events import Events
# from entidades.game_object import GameObject
# from src.game_objects.pilar import Pilar
# from src.game_objects.parede import Parede

# import pickle

# class Manager:

#     object_id_counter = 1
#     objects : List[GameObject] = []
#     objeto_selecionado = None

#     def check_mouse_over_object() -> GameObject:
#         for o in Manager.objects:
#             if o.is_over(Events.MOUSE_POS):
#                 return o
#         return None

#     def save():
#         f = open('planta.pk', 'wb')
#         pickle.dump(Manager.objects, f)
#         f.close()
    
#     def load():
#         f = open('planta.pk', 'rb')
#         Manager.objects = pickle.load(f)
#         for o in Manager.objects:
#             if o.id > Manager.object_id_counter:
#                 Manager.object_id_counter = o.id + 1
#         f.close()

#     def add(obj: GameObject):
#         Manager.objects.append(obj)
#         Manager.object_id_counter += 1
    
#     def remove(id: int):
#         Manager.objects = list(filter(lambda x: x.id != id, Manager.objects))

#     def update():

#         obj = Manager.check_mouse_over_object()

#         if Events.KEY_S_DOWN:
#             Manager.save()
#         if Events.KEY_L_DOWN:
#             Manager.load()
        
#         if Events.MOUSE_LEFT_BUTTON_DOWN:
#             if obj is None:
#                 pilar = Pilar(Manager.object_id_counter, Events.MOUSE_POS)
#                 pilar.set_selected(True)
#                 Manager.add(pilar)
#             elif isinstance(obj, Pilar):
#                 if Events.CTRL_PRESSED:
#                     obj.set_selected(True)
#                 else:
#                     parede = Parede(Manager.object_id_counter, obj.posicao, obj.posicao)
#                     parede.inicio = obj
#                     Manager.objeto_selecionado = parede
#                     Manager.add(parede)
        
#         if Events.MOUSE_MOVING:
#             if Manager.objeto_selecionado is not None and isinstance(Manager.objeto_selecionado, Parede):
#                 Manager.objeto_selecionado.posicao_fim = Events.MOUSE_POS

#         if Events.MOUSE_LEFT_BUTTON_UP:
#             if Manager.objeto_selecionado is not None and isinstance(Manager.objeto_selecionado, Parede):
#                 if isinstance(obj, Pilar):
#                     Manager.objeto_selecionado.fim = obj
#                     Manager.objeto_selecionado.posicao_fim = obj.posicao
#                 else:
#                     Manager.remove(Manager.objeto_selecionado.id)
#                 Manager.objeto_selecionado = None
            
#             for o in Manager.objects:
#                 o.set_selected(False)

#         if Events.MOUSE_RIGHT_BUTTON_DOWN:
#             if isinstance(obj, Pilar):
#                 Manager.remove(obj.id)
#             if isinstance(obj, Parede):
#                 Manager.remove(obj.id)

#         for o in Manager.objects:
#             o.update()
    
#     def render():
#         for o in Manager.objects:
#             o.render()