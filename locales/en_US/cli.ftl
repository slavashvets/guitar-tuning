# General Labels
guitar-tuning-analysis = Guitar Tuning Analysis
string_title = String { $name } (Open: { $open_freq } Hz)
fret = Fret
deviation = Deviation (cents)

# Grouped Averages and Recommendations
grouped_averages = Grouped Averages:
low = Low (1,3): { $value } cents
mid = Mid (5,7): { $value } cents
high = High (9,12): { $value } cents

recommendations = Recommendations:
saddle = Saddle: { $recommendation }
nut = Nut: { $recommendation }
bridge = Bridge: { $recommendation }
truss_diff = Truss diff (Mid - High): { $value } cents

# Overall Recommendation
overall_recommendation = Overall Truss Rod Recommendation:
average_truss_diff = Average Truss Diff (Mid - High): { $value } cents
overall = Overall

# Messages for string adjustments
saddle_sharp_significant = Notes at high frets are significantly sharp. Move the saddle backward (scale length too short).
saddle_sharp_slight = Notes at high frets are slightly sharp. Consider a slight backward adjustment of the saddle.
saddle_flat_significant = Notes at high frets are significantly flat. Move the saddle forward (scale length too long).
saddle_flat_slight = Notes at high frets are slightly flat. Consider a slight forward adjustment of the saddle.
saddle_perfect = High frets are perfectly tuned; no saddle adjustment needed.

nut_sharp_significant = Low frets are significantly sharp relative to high frets. Lower the nut.
nut_sharp_slight = Low frets are slightly sharp relative to high frets. Consider slightly lowering the nut.
nut_flat_significant = Low frets are significantly flat relative to high frets. Raise the nut.
nut_flat_slight = Low frets are slightly flat relative to high frets. Consider slightly raising the nut.
nut_perfect = Low and high fret deviations are equal; no nut adjustment needed.

bridge_high = The string height at the bridge is too high. Lower the saddle (reduce string height at the bridge).
bridge_low = The string height at the bridge is too low. Raise the saddle (increase string height at the bridge).
bridge_normal = String height at the bridge is within normal range.

mid_sharp_significant = Mid frets are significantly sharp relative to high frets. Reduce neck relief by tightening the truss rod ({ $direction } adjustment).
mid_sharp_slight = Mid frets are slightly sharp relative to high frets. Consider a slight truss rod adjustment.
mid_flat_significant = Mid frets are significantly flat relative to high frets. Increase neck relief by loosening the truss rod ({ $direction } adjustment).
mid_flat_slight = Mid frets are slightly flat relative to high frets. Consider a slight truss rod adjustment.
no_adjustment = Neck relief is optimal; no truss rod adjustment is needed.

truss_tip = Tip: Rotate the truss rod { $direction } by { $turns ->
    [one] { $turns } turn (about { $degrees }°).
   *[other] { $turns } turns (about { $degrees }°).
}

# Direction labels
clockwise = clockwise
counterclockwise = counterclockwise

# String label
string = String
