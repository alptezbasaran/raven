'''
Created on December 1, 2015

'''
from __future__ import division, print_function, unicode_literals, absolute_import
import warnings
warnings.simplefilter('default',DeprecationWarning)

from PostProcessorInterfaceBaseClass import PostProcessorInterfaceBase

class testInterfacedPP_PointSet(PostProcessorInterfaceBase):
  """ This class represents the most basic interfaced post-processor
      This class inherits form the base class PostProcessorInterfaceBase and it contains the three methods that need to be implemented:
      - initialize
      - run
      - readMoreXML
  """

  def initialize(self):
    """
     Method to initialize the Interfaced Post-processor
     @ In, None,
     @ Out, None,

    """
    PostProcessorInterfaceBase.initialize(self)
    self.inputFormat  = 'PointSet'
    self.outputFormat = 'PointSet'

  def run(self,inputDic):
    """
    This method is transparent: it passes the inputDic directly as output
     @ In, inputDic, dict, dictionary which contains the data inside the input DataObject
     @ Out, inputDic, dict, same inputDic dictionary

    """
    return inputDic

  def readMoreXML(self,xmlNode):
    """
      Function that reads elements this post-processor will use
      @ In, xmlNode, ElementTree, Xml element node
      @ Out, None
    """
    for child in xmlNode:
      if child.tag == 'xmlNodeExample':
        self.xmlNodeExample = child.text
