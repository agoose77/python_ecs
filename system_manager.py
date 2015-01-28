class SystemManager:
    
    def __init__(self):
        self.systems = []
        
    def add_entity(self, entity):
        components = entity.components
        
        for system, system_components in self.find_relevant_systems(components):
            system.entities[entity] = system_components
    
    def find_relevant_systems(self, components):        
        for system in self.systems:
            required_components = system.required_components
            components_for_system = {n: c for n, c in components.items() if n in required_components}
            
            if len(components_for_system) == len(required_components):
                yield system, components_for_system
        
    def remove_entity(self, entity):
        for system, _ in self.find_relevant_systems(entity):
            system.entities.remove(entity)  
    
    def update(self, delta_time):
        for system in self.systems:
            system.update(delta_time)
