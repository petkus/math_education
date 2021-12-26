# Harmonic Oscilator
This script generates an interactive visualizer of the solution to the harmonic oscillator equation
<p align="center"><img src="svgs/9613e36e319d3f848015d8b9ae77ad93.svg?invert_in_darkmode" align=middle width=177.9167214pt height=17.2895712pt/></p>
with initial conditions <img src="svgs/2361f6d3957971d029141bbf0b7360fd.svg?invert_in_darkmode" align=middle width=117.46560704999999pt height=24.7161288pt/>.
To run this code, type the command 

`python3 harmonic_oscillator.py` 

in the directory containing the file.

The output should look something like the following image. There are three slider bars for each of the three unkown constants <img src="svgs/98eee5e6717040513d097cf59600e42a.svg?invert_in_darkmode" align=middle width=30.37133054999999pt height=22.831056599999986pt/> and <img src="svgs/ae4fb5973f393577570881fc24fc2054.svg?invert_in_darkmode" align=middle width=10.82192594999999pt height=14.15524440000002pt/>.
<img src="svgs/example.png">



## Zero Friction Situation (<img src="svgs/edad3500d9f7368f82c110d98051b30b.svg?invert_in_darkmode" align=middle width=39.56070194999999pt height=21.18721440000001pt/>)
The solution to the homogeneous equation <img src="svgs/569dfb5fad34443cd6ea8ab70528198c.svg?invert_in_darkmode" align=middle width=86.49520109999999pt height=24.7161288pt/> has
natural frequency <img src="svgs/2d5a3da16b829a8256785ad582059cdd.svg?invert_in_darkmode" align=middle width=62.29826294999999pt height=29.33328419999998pt/>. When the forcing frequency is not equal to the natural frequency (i.e. <img src="svgs/76768489a51601052b262aee53e1c701.svg?invert_in_darkmode" align=middle width=49.52421539999999pt height=22.831056599999986pt/>), then the solution is proportional to
<p align="center"><img src="svgs/9f51c33c109e4d08301b1cbaca48b5b5.svg?invert_in_darkmode" align=middle width=251.9502183pt height=39.452455349999994pt/></p>
the smaller frequency <img src="svgs/7412e5be6b325dc4838f63eb017a5566.svg?invert_in_darkmode" align=middle width=77.74354004999998pt height=24.65753399999998pt/> contributes to the phenomenon of beats displayed below
<img src="svgs/beats.png">

As forcing frequency <img src="svgs/ae4fb5973f393577570881fc24fc2054.svg?invert_in_darkmode" align=middle width=10.82192594999999pt height=14.15524440000002pt/> the approaches the natural frequency <img src="svgs/747fe3195e03356f846880df2514b93e.svg?invert_in_darkmode" align=middle width=16.78467779999999pt height=14.15524440000002pt/> we get the phenomenon of resonance displayed below
<p align="center"><img src="svgs/f121536660a87adf0d09384ea01a79f0.svg?invert_in_darkmode" align=middle width=378.29012924999995pt height=39.452455349999994pt/></p>

<img src="svgs/resonance.png">

## Nonzero Friction Situation (<img src="svgs/e74f84cf82bd82054312a04d544ef340.svg?invert_in_darkmode" align=middle width=39.56070194999999pt height=21.18721440000001pt/>)
It is the case  solution is a sum <img src="svgs/a23e7513a1232936d0a8ada6e4cf88a2.svg?invert_in_darkmode" align=middle width=85.48818794999998pt height=19.1781018pt/> where <img src="svgs/0957a9bbf01d2ea5f621f1d068d404d9.svg?invert_in_darkmode" align=middle width=16.17146519999999pt height=14.15524440000002pt/> is a particular
solution tothe equation <img src="svgs/142de1ff09f58b1111899d44c6655f34.svg?invert_in_darkmode" align=middle width=173.35049655pt height=24.7161288pt/> and  <img src="svgs/3af6bfdea3e15c6b28624c7052e83e4f.svg?invert_in_darkmode" align=middle width=17.09101514999999pt height=14.15524440000002pt/> is
a solution to the homogeneous equation <img src="svgs/6ac28605ca60a42d6cf36a602fa9b5d6.svg?invert_in_darkmode" align=middle width=130.01711744999997pt height=24.7161288pt/>. It is the
case the limit of the homogeneous solution is zero; <img src="svgs/38dbc905c6f321f8a526ca4ab2f9d68f.svg?invert_in_darkmode" align=middle width=124.3398849pt height=24.65753399999998pt/>. Thus <img src="svgs/45ef8549fa6a14179b842e3f10821a16.svg?invert_in_darkmode" align=middle width=36.63445994999999pt height=24.65753399999998pt/> can be thought of some transient interference and for
sufficiently large <img src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode" align=middle width=5.936097749999991pt height=20.221802699999984pt/>, <img src="svgs/aabf954e1b9d8a0035ba2b9719862fac.svg?invert_in_darkmode" align=middle width=85.74904305pt height=24.65753399999998pt/>. One can show (for instance via the method of undetermined coefficients) that <img src="svgs/0957a9bbf01d2ea5f621f1d068d404d9.svg?invert_in_darkmode" align=middle width=16.17146519999999pt height=14.15524440000002pt/> is of the form 
<p align="center"><img src="svgs/e0a1057438cc5702c9eab99a70f83a50.svg?invert_in_darkmode" align=middle width=154.41897735pt height=17.031940199999998pt/></p>
An example of this phenomenon is pictured below
<img src="svgs/damped.png">

