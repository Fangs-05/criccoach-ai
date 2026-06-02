def generate_coaching_report(tips, overall_score, player_name="Player"):
    """
    Generates full NLP coaching report from scored tips
    Returns structured report dictionary
    """
    
    # Filter out obscured areas from the standard logic
    obscured_areas = [t for t in tips if '[Obscured]' in t['area']]
    weak_areas = [t for t in tips if t['score'] < 8 and '[Obscured]' not in t['area']]
    good_areas = [t for t in tips if t['score'] >= 8 and '[Obscured]' not in t['area']]

    # Opening summary based on score
    if overall_score >= 85:
        opening = (
            f"{player_name}, your form is excellent! "
            f"You scored {overall_score}/100. "
            f"Your technique shows strong fundamentals. "
            f"Focus on the minor refinements below to reach peak form."
        )
    elif overall_score >= 70:
        opening = (
            f"{player_name}, you have a solid foundation with a score of {overall_score}/100. "
            f"There are {len(weak_areas)} area(s) to work on. "
            f"With focused practice on the points below, you can significantly improve."
        )
    elif overall_score >= 55:
        opening = (
            f"{player_name}, your score is {overall_score}/100 — average level. "
            f"You have {len(good_areas)} strong areas but {len(weak_areas)} areas need attention. "
            f"Consistent practice on the corrections below will make a big difference."
        )
    else:
        opening = (
            f"{player_name}, your score is {overall_score}/100. "
            f"Focus on one correction at a time, starting with the most critical area below."
        )

    # Priority corrections
    corrections = []
    for i, tip in enumerate(weak_areas, 1):
        drill = get_drill(tip['area'])
        corrections.append({
            'priority': i,
            'area': tip['area'],
            'your_angle': tip['your_angle'],
            'ideal': tip['ideal'],
            'problem': tip['tip'],
            'drill': drill
        })

    # Strengths
    strengths = []
    for tip in good_areas:
        strengths.append({
            'area': tip['area'],
            'message': tip['tip']
        })
        
    # Warnings for obscured joints
    warnings = []
    for tip in obscured_areas:
        warnings.append({
            'area': tip['area'],
            'message': tip['tip']
        })

    # Closing advice
    if len(weak_areas) == 0:
        closing = (
            "Outstanding technique! Keep practicing consistently to maintain this form. "
            "Consider recording yourself regularly to track any drift in your stance."
        )
    elif len(weak_areas) <= 2:
        closing = (
            f"You are close to excellent form. Focus your next 3 practice sessions specifically "
            f"on {weak_areas[0]['area']}. Small corrections lead to big improvements."
        )
    else:
        closing = (
            f"Start with Priority 1 — {weak_areas[0]['area']}. "
            f"Master one correction before moving to the next. "
            f"Re-analyze your stance every week to track progress."
        )

    return {
        'player_name': player_name,
        'overall_score': overall_score,
        'opening': opening,
        'corrections': corrections,
        'strengths': strengths,
        'warnings': warnings,
        'closing': closing,
        'session_tip': get_session_tip(overall_score)
    }


def get_drill(area):
    """Returns specific practice drill for each weak area using keyword matching"""
    area_lower = area.lower()
    
    if 'lead elbow' in area_lower:
        return (
            "Shadow batting drill: Stand in front of a mirror and practice your "
            "swing 20 times. Focus on keeping your lead elbow high and extended. "
            "Use a lightweight bat for this drill."
        )
    elif 'back elbow' in area_lower:
        return (
            "Wall drill: Stand 1 foot from a wall. Practice your batting stance "
            "ensuring your back elbow does not touch the wall or flare out. "
            "Repeat 15 times focusing on tucked elbow position."
        )
    elif 'lead knee' in area_lower or 'front knee' in area_lower:
        return (
            "Stance hold drill: Get into your batting stance and hold it for 30 seconds. "
            "Check that your lead knee has a slight bend and weight is transferring correctly. "
            "Repeat 10 times."
        )
    elif 'back knee' in area_lower:
        return (
            "Squat stance drill: Practice moving from a normal stance to a lower "
            "crouched position. Find the comfortable midpoint where your back knee "
            "provides a solid, stable base. Hold 20 seconds, repeat 8 times."
        )
    elif 'trunk' in area_lower or 'lean' in area_lower:
        return (
            "Forward press drill: Practice a slight forward press before each "
            "imaginary delivery. Your weight should shift forward naturally. "
            "Do 25 repetitions with a partner calling 'press' randomly."
        )
    elif 'shoulder' in area_lower:
        return (
            "Mirror drill: Stand in front of a mirror in batting stance. "
            "Place a ruler or bat across your shoulders and check it is level. "
            "Adjust until level and hold 30 seconds. Repeat 10 times."
        )
    elif 'head' in area_lower:
        return (
            "Head still drill: Place a cricket ball on top of your head while "
            "practicing your stance. Try to keep it balanced for 20 seconds. "
            "This trains head stillness and keeping your eyes level."
        )
        
    return (
        "Practice this position in front of a mirror for 10 minutes daily. "
        "Focus on holding the correct form for 30 seconds at a time."
    )


def get_session_tip(score):
    """Returns today's session recommendation"""
    if score >= 85:
        return "Today's focus: Record yourself facing 20 deliveries and compare your form."
    elif score >= 70:
        return "Today's focus: Spend 15 minutes on mirror drills for your weakest area."
    elif score >= 55:
        return "Today's focus: Shadow batting for 20 minutes focusing on your fundamentals."
    else:
        return "Today's focus: Work with a coach or experienced player on basic mechanics."


def format_report_text(report):
    """Formats report as readable text"""
    lines = []
    lines.append("=" * 50)
    lines.append("      CRICCOACH AI — COACHING REPORT")
    lines.append("=" * 50)
    lines.append(f"\n{report['opening']}\n")

    if report['corrections']:
        lines.append("-" * 50)
        lines.append("CORRECTIONS NEEDED:")
        lines.append("-" * 50)
        for c in report['corrections']:
            lines.append(f"\nPriority {c['priority']}: {c['area']}")
            lines.append(f"  Your angle : {c['your_angle']}°")
            lines.append(f"  Ideal range: {c['ideal']}")
            lines.append(f"  Problem    : {c['problem']}")
            lines.append(f"  Drill      : {c['drill']}")

    if report['strengths']:
        lines.append(f"\n{'-' * 50}")
        lines.append("YOUR STRENGTHS:")
        lines.append("-" * 50)
        for s in report['strengths']:
            lines.append(f"  ✅ {s['area']}: {s['message']}")
            
    if report.get('warnings'):
        lines.append(f"\n{'-' * 50}")
        lines.append("ANALYSIS WARNINGS:")
        lines.append("-" * 50)
        for w in report['warnings']:
            lines.append(f"  ⚠️ {w['area']}: {w['message']}")

    lines.append(f"\n{'=' * 50}")
    lines.append(f"COACH'S CLOSING NOTE:")
    lines.append(report['closing'])
    lines.append(f"\nTODAY'S SESSION TIP:")
    lines.append(report['session_tip'])
    lines.append("=" * 50)

    return "\n".join(lines)