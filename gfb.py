from bestia.output import Row, FString, echo

from notes import *
from scales import *

class String(object):

    # fret = [] # WHY IS THIS SHARED BETWEEN MY STRING OBJECTS???
    _DISPLAY_FRETS = 1 +12

    def __init__(self, tone, alt='', octave=0):

        open_note = Note(tone, alt, octave)
        scale_generator = ChromaticScale(
            open_note.tone,
            open_note.alt
        ).scale(notes=self._DISPLAY_FRETS)

        self.fret = []
        for degree in scale_generator:
            self.fret.append(degree)

    def __repr__(self):
        string_line = Row()

        for fret, note in enumerate(self.fret):

            sz = 4 if fret == 0 else 6
            note = FString(
                '{}{}{}'.format(note.tone, note.alt, note.octave),
                size=sz, align='cr', colors=['blue']
            )

            string_line.append(note)

            sep = FString(
                '|' if fret == 0 or fret == 12 else '¦'
            )
            string_line.append(sep)
        
        return str(string_line)


class Guitar(object):

    tuners = '     '
    # tuners = 'O  O  O  '

    longness = 83

    @classmethod
    def binding(cls, side='lower'):
        _binding = '_' if side == 'upper' else '‾'
        echo(cls.tuners + _binding * cls.longness)

    @classmethod
    def fret_markers(cls, complete=False):

        i = 'I' if complete else ''
        ii = 'II' if complete else ''
        iv = 'IV' if complete else ''
        vi = 'VI' if complete else ''
        vi = 'VI' if complete else ''
        viii = 'VIII' if complete else ''
        x = 'X' if complete else ''
        xi = 'XI' if complete else ''

        r = Row(
            FString('', size=5),
            FString(i, size=7, align='cl', colors=['magenta'], pad=None),
            FString(ii, size=7, align='cl', colors=['magenta']),
            FString('III', size=7, align='cl', colors=['magenta']),
            FString(iv, size=7, align='cl', colors=['magenta']),
            FString('V', size=7, align='cl', colors=['magenta']),
            FString(vi, size=7, align='cl', colors=['magenta']),
            FString('VII', size=7, align='cl', colors=['magenta']),
            FString(viii, size=7, align='cl', colors=['magenta']),
            FString('IX', size=7, align='cl', colors=['magenta']),
            FString(x, size=7, align='cl', colors=['magenta']),
            FString(xi, size=7, align='cl', colors=['magenta']),
            FString('XII', size=7, align='cl', colors=['magenta']),
            width=len(cls.tuners) +cls.longness
        ).echo()

    def __init__(self, *arg, **kwargs):

        self.strings = []

        # FILTER STRING ARGS
        string_args = dict( [(k.replace('string', ''), note) for k, note in kwargs.items() if k.startswith('string')] )

        self._init_strings(len(string_args))
        self._assign_strings(string_args)

    ### INIT FUNCTIONS

    def _init_strings(self, string_count):
        for n in range(string_count):
            self.strings.append(None)

    def _assign_strings(self, string_args):
        for k, note in string_args.items():
            self.strings[int(k) -1] = String(
                note.tone, note.alt, note.octave
            )

    ### REPR FUNCTIONS

    def fretboard(self):
        self.fret_markers()
        self.binding('upper')
        for s in self.strings:
            echo(s)
        self.binding('lower')


    def string(self, s):
        return self.strings[s -1]

    # def echo_string(self, s):
    #     echo(self.string(s))

def unit_test(s):
    for _row in ENHARMONIC_MATRIX:
        for _enharmonic_note in _row:
            if len(_enharmonic_note.alt) >1 or '?' in _enharmonic_note.alt:
                continue
            echo(_enharmonic_note, 'blue')
            echo(s(_enharmonic_note.tone, _enharmonic_note.alt), 'cyan')

if __name__ == '__main__':

    try:
        # a_minor = MelodicMinorScale('A')
        # print(a_minor)

        # d_minor = HarmonicMinorScale('D')
        # print(d_minor)

        std_tuning = Guitar(
            string1=Note('G', 'b', 4),
            string2=Note('B', '', 3),
            string3=Note('G', '', 3),
            string4=Note('D', '', 3),
            string5=Note('A', '', 2),
            string6=Note('E', '', 2),
        )

        std_tuning.fretboard()
        # echo(std_tuning.string(4))



        # s = String('E', '', 4)
        # echo(s, 'green')


        # empty_fret = Fret(fret=6)
        # string1 = Row(
        #     empty_fret, 
        #     # FString(empty_fret, size=6, align='r'),
        #     width=72
        # ).echo()

        # unit_test(ChromaticScale)
        # unit_test(MajorScale)
        # unit_test(NaturalMinorScale)
        # unit_test(MelodicMinorScale)
        # unit_test(HarmonicMinorScale)

        # a_major = MinorScale('A')
        # for n in a_major.ninth():
        #     print(n)

    except KeyboardInterrupt:
        echo()


# JUST FINISHED BASIC CHROMATIC SCALE DEFINITION TO OUTPUT ALL FRETS OF STRING
