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


class cortex(baseLib):
    def versions(self):
        if self.parent() in 'gaffer':
            if float(pipe.version.get('gaffer')[:3]) < 2.0:
                if float(pipe.libs.version.get('cortex')[:1]) >= 9:
                    pipe.libs.version.set(  cortex = '8.4.7' )
                    pipe.libs.version.set(  boost = '1.5.2' )
                    pipe.libs.version.set(  tbb = '2.2.004' )

    def environ(self):
        parent = self.parent()
        
        self['PYTHON_VERSION_MAJOR'] = '.'.join(pipe.libs.version.get('python').split('.')[:2])
        
        # we add this env var for easy copy/paste of houdini paths into other apps/cortex!
        if pipe.admin.job.current():
            self['HIP'] = '$SHOT/houdini'

        
        # configure maya plugin/scripts/icons
        if parent == 'maya':
            maya.addon ( self,
                plugin = self.path('maya/$MAYA_VERSION/plugins'),
                script = self.path('maya/$MAYA_VERSION/mel'),
                icon   = self.path('maya/$MAYA_VERSION/icons'),
                lib = [
                    self.path('maya/$MAYA_VERSION/lib/python$PYTHON_VERSION_MAJOR'),
                    self.path('maya/$MAYA_VERSION/lib'),
                ],
            
            )
            self['PYTHONPATH'] = self.path('maya/$MAYA_VERSION/lib/python$PYTHON_VERSION_MAJOR/site-packages')
        
        #configure delight
        if parent in ['delight', 'maya', 'gaffer', 'python']:
            delight.addon( self, 
                shader=self.path('delight/$DELIGHT_VERSION/rsl'), 
                rsl=self.path('delight/$DELIGHT_VERSION/rsl'),
                procedurals=self.path('delight/$DELIGHT_VERSION/procedurals'), 
                display=self.path('delight/$DELIGHT_VERSION/displays'), 
                texture='',
                lib = [
                    self.path('delight/$DELIGHT_VERSION/lib'),
                    self.path('delight/$DELIGHT_VERSION/lib/python$PYTHON_VERSION_MAJOR'),
                ],
            )
            self['PYTHONPATH'] = self.path('delight/$DELIGHT_VERSION/lib/python$PYTHON_VERSION_MAJOR')
            self['PYTHONPATH'] = self.path('delight/$DELIGHT_VERSION/lib/python$PYTHON_VERSION_MAJOR/site-packages')

        #configure arnold
        if parent in ['arnold', 'maya']:
            arnold.addon( self, 
                procedurals=self.path('arnold/$ARNOLD_VERSION/procedurals'), 
                display=self.path('arnold/$ARNOLD_VERSION/displays'), 
                extensions=self.path('arnold/$ARNOLD_VERSION/mtoaExtensions/$MAYA_VERSION/'), 
                lib = [
                    self.path('arnold/$ARNOLD_VERSION/lib/python$PYTHON_VERSION_MAJOR'),
                    self.path('arnold/$ARNOLD_VERSION/lib'),
                ],
            )
            self['PYTHONPATH'] = self.path('arnold/$ARNOLD_VERSION/lib/python$PYTHON_VERSION_MAJOR/site-packages')
        
        #configure nuke
        if parent == 'nuke':
            nuke.addon( self, 
                nukepath = self.path('nuke/$NUKE_VERSION/plugins'),
                lib = [
                    self.path('nuke/$NUKE_VERSION/lib/python$PYTHON_VERSION_MAJOR'),
                    self.path('nuke/$NUKE_VERSION/lib'),
                ],
            )
            self['PYTHONPATH'] = self.path('nuke/$NUKE_VERSION/lib/python$PYTHON_VERSION_MAJOR/site-packages')
        
        #configure houdini
        if parent in ['houdini', 'python']:
#            if parent == 'python':
#                self.update( houdini() )
            houdini.addon(self, 
                otl=self.path('houdini/$HOUDINI_VERSION/otls'), 
                dso=self.path('houdini/$HOUDINI_VERSION/dso'), 
                toolbar=self.path('houdini/$HOUDINI_VERSION/toolbar'), 
                icon=self.path('houdini/$HOUDINI_VERSION/icons'),
                lib = [
                    self.path('houdini/$HOUDINI_VERSION/lib/python$PYTHON_VERSION_MAJOR'),
                    self.path('houdini/$HOUDINI_VERSION/lib'),
                ],
            )
            self['PYTHONPATH'] = self.path('houdini/$HOUDINI_VERSION/lib/python$PYTHON_VERSION_MAJOR/site-packages')
            
        #configure python
        self['PYTHONPATH'] = self.path('lib/python$PYTHON_VERSION_MAJOR/site-packages')        
            
        
        #add cortex paths
        cortex.addon(self, 
#            scripts = self.path('lib/python$PYTHON_VERSION_MAJOR/site-packages'),
            procedurals = self.path('procedurals'),
            ops = self.path('ops'),
            glsl = self.path('glsl'),
            glslInclude = self.path('glsl'),
            lib = [
                self.path('lib/python$PYTHON_VERSION_MAJOR'),
                self.path('lib'),
                self.path('alembic/1.1.1'),
            ]
        )
        
        #add tools paths
        for each in self.toolsPaths():
            studio = ""
#            studio = "$STUDIO"
            if 'jobs' in each:
                studio = ""
            cortex.addon(self, 
                procedurals = [
                        '%s/cortex/procedurals/%s' % (each, studio),
                        '%s/cortex/$CORTEX_VERSION/procedurals/%s' % (each, studio),
                ],
                ops = [
                       '%s/cortex/ops/%s' % (each, studio),
                       '%s/cortex/$CORTEX_VERSION/ops/%s' % (each, studio),
                ],
                glsl = '%s/cortex/glsl' % each,
                glslInclude = '%s/cortex/glsl/include' % each,
                glFonts = '%s/cortex/fonts' % each,
            )     
            self['IECORE_ASSET_OP_PATHS'] = '%s/config/assets' % each

        self['IECORE_OP_PRESET_PATHS'] = '%s/.config/cortex/preset' % os.environ['HOME']
        self['IECORE_PROCEDURAL_PRESET_PATHS'] = '%s/.config/cortex/preset' % os.environ['HOME']

    def bins(self):
        return [('cpython', 'cpython')]

        
    @staticmethod
    def addon(caller, ops="", procedurals="", scripts="", glsl="", glslInclude="", glslTextures="", glFonts="", lib=""):
        caller['IECORE_PROCEDURAL_PATHS'] = procedurals
        caller['IECORE_OP_PATHS']  = ops
        caller['PYTHONPATH']  = scripts
        caller['IECOREGL_SHADER_PATHS'] = glsl
        caller['IECOREGL_SHADER_INCLUDE_PATHS'] = glslInclude
        caller['IECOREGL_TEXTURE_PATHS'] = glslTextures
        caller['IECORE_FONT_PATHS'] = glFonts
        caller['LD_LIBRARY_PATH'] = lib

