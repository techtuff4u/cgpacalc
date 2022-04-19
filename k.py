from flask import*


s = Flask(__name__)

@s.route("/")
def hi():
    return render_template("index.html")

@s.route("/hi", methods=["POST"])
def input():
    dept=request.form["dep"]
    dept=dept.upper()
    sem=request.form["sem"]
    if (dept == "IT"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("input.html", a=a)
        elif (sem == "2"):


            g = [["MA1202", 4], ["PH1252", 3], ["GE1204", 3], ["BE1251", 4], ["HS1201", 3], ["GE1206", 3],
                 ["GE1207", 2], ["CS1208", 2]]
            a=(("MA1202"), ("PH1252"), ("GE1204"), ("BE1251"), ("HS1201"), ("GE1206"),
               ("GE1207"), ("CS1208"))
            return render_template("input.html", a=a)
    elif (dept == "ECE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "EEE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "CSE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "CHEMICAL"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "MECH"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "BIOTECH"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "EIE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)
    elif (dept == "AIML"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "AIDS"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)

    elif (dept == "CIVIL"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))
            return render_template("input.html", a=a)





@s.route("/result",methods=["POST"])

def result():
    dept = request.form["dep"]
    dept = dept.upper()
    sem = request.form["sem"]

    def gpa(c):

        l = []
        s = []

        for i in range(0, 8):
            x = c[i][1]
            l.append(x)
            j = request.form[c[i][0]]
            s.append(j)
        s = [x.upper() for x in s]
        for i in range(len(s)):
            if (s[i] == "O"):
                s[i] = 10
            elif (s[i] == "A+"):
                s[i] = 9
            elif (s[i] == "A"):
                s[i] = 8
            elif (s[i] == "B+"):
                s[i] = 7
            elif (s[i] == "B"):
                s[i] = 6

        a = []
        for i in range(len(s)):
            a.append([])
            for j in range(len(s)):
                if (i == j):
                    a[j].append(l[j])
                    a[j].append(s[j])



        d = []

        for i in range(len(c)):
            score = a[i][0] * a[i][1]
            d.append(score)
        
        total = sum(d)
        print(total)
        tc = []
        for i in range(len(c)):
            tc.append(c[i][1])
        sumc = sum(tc)
        print(sumc)
        gpa = total / sumc
        return (gpa)

    def cgpa(c1, c2):
        cgpa = (c1 + c2) / 2
        return render_template("GCPA Calculator 1.html", result=cgpa)

    if (dept == "IT"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html",result=gpa(g))
        elif (sem == "2"):


            g = [["MA1202", 4], ["PH1252", 3], ["GE1204", 3], ["BE1251", 4], ["HS1201", 3], ["GE1206", 3],
                 ["GE1207", 2], ["CS1208", 2]]
            a=(("MA1202"), ("PH1252"), ("GE1204"), ("BE1251"), ("HS1201"), ("GE1206"),
               ("GE1207"), ("CS1208"))
            return render_template("result.html", result=gpa(g))
    elif (dept == "ECE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "EEE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "CSE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "CHEMICAL"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "MECH"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "BIOTECH"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "EIE"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "AIML"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "AIDS"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
    elif (dept == "CIVIL"):
        if (sem == "1"):
            g = [["MA1102", 4], ["PH1103", 3], ["CY1104", 3], ["GE1105", 3], ["HS1101", 3], ["GE1106", 4],
                 ["GE1107", 2], ["BS1108", 2]]
            a = (("MA1102"), ("PH1103"), ("CY1104"), ("GE1105"), ("HS1101"), ("GE1106"), ("GE1107"), ("BS1108"))

            return render_template("result.html", result=gpa(g))
if __name__ == "__main__":
    s.run(debug=True)
