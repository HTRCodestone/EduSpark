//
//  MainPage.swift
//  EduSpark
//
//  Created by Logan Dhillon on 2023-12-09.
//

import SwiftUI

struct MainPage: View {
    var body: some View {
        ZStack() {
            Text("All of your child's learning ")
                .foregroundColor(textColor)
                .multilineTextAlignment(.center)
                .font(Font.custom("Helvetica Neue", size: 128).weight(.bold))
                .offset(y: -125)
            Text("in ")
                .foregroundColor(textColor)
                .font(Font.custom("Helvetica Neue", size: 128).weight(.bold)) +
            Text("one")
                    .foregroundColor(Color(red: 0.9176470588235294, green: 0.7019607843137254, blue: 0.03137254901960784))
                    .font(Font.custom("Helvetica Neue", size: 128).weight(.bold)) +
            Text(" place")
                .foregroundColor(textColor)
                .font(Font.custom("Helvetica Neue", size: 128).weight(.bold))
            ZStack() {
                Rectangle()
                    .foregroundColor(.clear)
                    .frame(width: 540, height: 128)
                    .background(Color(red: 0.01, green: 0.52, blue: 0.78))
                    .cornerRadius(16)
                    .offset(x: 0, y: 0)
                Text("Sign up")
                    .font(Font.custom("Helvetica Neue", size: 48).weight(.bold))
                    .foregroundColor(Color(red: 0.89, green: 0.91, blue: 0.94))
                    .offset(x: 0, y: 0)
            }
            .frame(width: 540, height: 128)
            .offset(x: -286, y: 189)
            ZStack() {
                Rectangle()
                    .foregroundColor(.clear)
                    .frame(width: 540, height: 128)
                    .background(Color(red: 0.65, green: 0.95, blue: 0.99))
                    .cornerRadius(16)
                    .offset(x: 0, y: 0)
                Text("Learn more")
                    .font(Font.custom("Helvetica Neue", size: 48).weight(.bold))
                    .foregroundColor(Color(red: 0.06, green: 0.09, blue: 0.16))
                    .offset(x: 0, y: 0)
            }
            .frame(width: 540, height: 128)
            .offset(x: 286, y: 189)
            Image("Logo")
                .offset(x: -750, y: -475)
            ZStack() {
                Rectangle()
                    .foregroundColor(.clear)
                    .frame(width: 128, height: 64)
                    .background(Color(red: 0.09, green: 0.15, blue: 0.33))
                    .cornerRadius(16)
                    .offset(x: 0, y: 0)
                Text("Log in")
                    .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                    .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                    .offset(x: 0, y: 0)
            }
            .frame(width: 128, height: 64)
            .offset(x: 704, y: -476)
            ZStack() {
                Rectangle()
                    .foregroundColor(.clear)
                    .frame(width: 128, height: 64)
                    .background(Color(red: 0.01, green: 0.52, blue: 0.78))
                    .cornerRadius(16)
                    .offset(x: 0, y: 0)
                Text("Sign up")
                    .font(Font.custom("Helvetica Neue", size: 24).weight(.bold))
                    .foregroundColor(Color(red: 0.88, green: 0.95, blue: 1))
                    .offset(x: 0, y: 0)
            }
            .frame(width: 128, height: 64)
            .offset(x: 864, y: -476)
            Rectangle()
                .foregroundColor(.clear)
                .frame(width: 302.91, height: 44.80)
                .background(
                    AsyncImage(url: URL(string: "https://via.placeholder.com/303x45"))
                )
                .offset(x: -776.54, y: -475.60)
        }
        .frame(width: 1920, height: 1080)
        .background(Color(red: 0.96, green: 0.96, blue: 0.96))
    }
}

#Preview {
    MainPage()
}
