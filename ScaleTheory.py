# Brant Buckley
# Class: Intro to Python
# File: ScaleTheory.py
# Date: 5/01/22
# Description: A class called ScaleTheory with the following attributes: major scale, major scale chords,
# major scale's relative minor scale and relative minor chords. The relative minor
# scale and chords start on the 6th degree of the major scale. The minor scale is relative to
# its major scale, hence called relative minor in relation to the major scale. In music, everything
# starts and is constructed from the major scale.

class ScaleTheory:
    ''' A class that describes makeup of scales'''
    
    # Initializing the potential object with 4 attributes.
    def __init__(self, majorScale, majorChords, relativeMinorscale, relativeMinorchords):
        ''' Initialize the object'''
        self.__majorScale = majorScale
        self.__majorChords = majorChords
        self.__relativeMinorscale = relativeMinorscale
        self.__relativeMinorchords = relativeMinorchords
        
    # Property Decorators with setters.
    # For: majorScale, majorChords, relativeMinorscale, relativeMinorchords.
    @property
    def majorScale(self):
        return self.__majorScale
    
    @majorScale.setter
    def majorScale(self, majorScale):
        self.__majorScale = majorScale
        
    @property
    def majorChords(self):
        return self.__majorChords
    
    @majorChords.setter
    def majorChords(self, majorChords):
        self.__majorChords = majorChords
    
    @property
    def relativeMinorscale(self):
        return self.__relativeMinorscale
    
    @relativeMinorscale.setter
    def relativeMinorscale(self, relativeMinorscale):
        self.__relativeMinorscale = relativeMinorscale
        
    @property
    def relativeMinorchords(self):
        return self.__relativeMinorchords
    
    @relativeMinorchords.setter
    def relativeMinorchords(self, relativeMinorchords):
        self.__relativeMinorchords = relativeMinorchords
        
    # 4 Methods: Majors, Minors, Scales, and Chords
    # That returns Majors, Minors, Scales, or Chords when called.
    def Majors(self):
         ''' Returns the major scale and major set of chords for any key when called '''
         return self.__majorScale, self.__majorChords
      
    def Minors(self):
         ''' Returns the relative minor scale and the relative minor set of chords when called '''
         return self.__relativeMinorscale, self.__relativeMinorchords 
    
    def Scales(self):
        ''' Returns both scales: The Major Scale and it's relative minor scale '''
        return self.__majorScale, self.__relativeMinorscale
    
    def Chords(self):
        ''' Returns both sets of chords: The major chords and relative minor chords '''
        return self.__majorChords, self.__relativeMinorchords
    
    # The __string__ method returns the object's state as a string.
    def __str__(self):
        return f'Major Scale: {self.__majorScale}\n' + \
               f'Major Chords: {self.__majorChords}\n' + \
               f'Relative Minor Scale: {self.__relativeMinorscale}\n' + \
               f'Relative Minor Chords: {self.__relativeMinorchords}'
               
      
        

