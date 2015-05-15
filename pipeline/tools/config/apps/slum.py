# =================================================================================
#    This file is part of pipeVFX.
#
#    pipeVFX is a software system initally authored back in 2006 and currently 
#    developed by Roberto Hradec - https://bitbucket.org/robertohradec/pipevfx
#
#    pipeVFX is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pipeVFX is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with pipeVFX.  If not, see <http://www.gnu.org/licenses/>.
# =================================================================================

class slum(baseApp):
    def environ(self):
        # configure maya plugin/scripts/icons
        maya.addon ( self,
            plugin = self.path('python'),
            script = self.path('python'),
            icon   = self.path('icons'),
        )

        self['SLUM_PATH'] = self.path()
        
        for each in self.toolsPaths():
            self['SLUM_SEARCH_PATH'] = '%s/shaders/slum/' % each

        
        self['SLUM_SEARCH_PATH'] = self.path('shader')