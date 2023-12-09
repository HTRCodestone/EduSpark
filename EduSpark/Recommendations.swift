//
//  Recommendations.swift
//  EduSpark
//
//  Created by Logan Dhillon on 2023-12-09.
//

import SwiftUI

struct Recommendations: View {
    var body: some View {
        ZStack() {
            Ellipse()
                .foregroundColor(.clear)
                .frame(width: 8, height: 8)
                .background(Color(red: 0.06, green: 0.09, blue: 0.16))
                .offset(x: 62, y: -661)
            HStack(spacing: 0) {
                ZStack() {
                    Text("Overview")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                        .offset(x: -629.50, y: 0)
                    Text("Recommendations")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                        .offset(x: -5, y: 0)
                    Text("Calendar")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                        .offset(x: 234, y: 0)
                    Text("Curriculum")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                        .offset(x: -434, y: 0)
                    Text("Absence")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                        .offset(x: -242, y: 0)
                    Text("SchoolCash")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                        .offset(x: 579, y: 0)
                    Rectangle()
                        .foregroundColor(.clear)
                        .frame(width: 24, height: 24)
                        .background(
                            AsyncImage(url: URL(string: "https://via.placeholder.com/24x24"))
                        )
                        .offset(x: 671, y: -0.50)
                }
                .frame(width: 1366, height: 29)
            }
            .padding(EdgeInsets(top: 2, leading: 0, bottom: 1, trailing: 4))
            .frame(width: 1370, height: 32)
            .offset(x: -0, y: -688)
            ZStack() {
                Group {
                    Rectangle()
                        .foregroundColor(.clear)
                        .frame(width: 1440, height: 1305)
                        .background(Color(red: 0.09, green: 0.15, blue: 0.33))
                        .cornerRadius(32)
                        .offset(x: 0, y: 0)
                    Text("Report card summary")
                        .font(Font.custom("Helvetica Neue", size: 64).weight(.bold))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -340, y: 309.50)
                    Text("Recommendations for your child")
                        .font(Font.custom("Helvetica Neue", size: 64).weight(.bold))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -172.50, y: -569.50)
                    Text("Last updated Dec. 9, 2023")
                        .font(Font.custom("Helvetica Neue", size: 24))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -528.50, y: -509)
                    Text("ENG2D1")
                        .font(Font.custom("Helvetica Neue", size: 48))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -577, y: -434)
                    Text("Your child's progress in English is excellent and there is no need to improve it at the moment. They should consider asking their teacher for ways to boost their mark further if desired.")
                        .font(Font.custom("Helvetica Neue", size: 24))
                        .foregroundColor(Color(red: 1, green: 0.98, blue: 0.76))
                        .offset(x: 10, y: -365.80)
                    Text("MPM2D1")
                        .font(Font.custom("Helvetica Neue", size: 48))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -570, y: -269)
                    Text("Your child's progress in math is very good and there is no need to improve it at the moment. They should consider asking their teacher for ways to boost their mark further if desired.")
                        .font(Font.custom("Helvetica Neue", size: 24))
                        .foregroundColor(Color(red: 1, green: 0.98, blue: 0.76))
                        .offset(x: 40, y: -200.80)
                    Text("SNC2D1")
                        .font(Font.custom("Helvetica Neue", size: 48))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -582, y: -104)
                    Text("TEJ2O1")
                        .font(Font.custom("Helvetica Neue", size: 48))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -590, y: 89.60)
                }
                Group {
                    Text("Your child's progress in science is very good and there is no need to improve it at the moment. They should consider asking their teacher for ways to boost their mark further if desired.")
                        .font(Font.custom("Helvetica Neue", size: 24))
                        .foregroundColor(Color(red: 1, green: 0.98, blue: 0.76))
                        .offset(x: 10, y: -21.30)
                    Text("Your child's progress in computer technology is excellent and there is no need to improve it at the moment. They should consider asking their teacher for ways to boost their mark further if desired.")
                        .font(Font.custom("Helvetica Neue", size: 24))
                        .foregroundColor(Color(red: 1, green: 0.98, blue: 0.76))
                        .offset(x: 20, y: 157.80)
                    Text("Upload your child's report card and let GPT-4 provide you a detailed summary of your progress.")
                        .font(Font.custom("Helvetica Neue", size: 24))
                        .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                        .offset(x: -153, y: 391.84)
                    Text("POWERED BY")
                        .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                        .foregroundColor(Color(red: 0.65, green: 0.95, blue: 0.99))
                        .offset(x: 411, y: 603.60)
                    ZStack() {
                        Rectangle()
                            .foregroundColor(.clear)
                            .frame(width: 256, height: 96)
                            .background(Color(red: 0.65, green: 0.95, blue: 0.99))
                            .cornerRadius(4)
                            .offset(x: 0, y: 0)
                        Text("Upload")
                            .font(Font.custom("Helvetica Neue", size: 36).weight(.bold))
                            .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                            .offset(x: 0, y: 0)
                    }
                    .frame(width: 256, height: 96)
                    .offset(x: -544, y: 500.10)
                }
            }
            .frame(width: 1440, height: 1080)
            .offset(x: 0, y: 35.50)
        }
        .frame(width: 1920, height: 1080)
        .background(Color(red: 0.96, green: 0.96, blue: 0.96))
    }
}

#Preview {
    Recommendations()
}
