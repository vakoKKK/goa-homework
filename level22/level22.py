    რა არუს Git და Github

Git-ი არის ვერსიების კონტროლის სისტემა რომლის დახმარებით ვაკონტროლებთ ვერსიების განახლებას ჩვენს ფოლდერში.
Git-ის დახმარებით შეგვიძლია გუნდურად ვიმუშაოთ(კოლაბორაცია).
   Github-ი არის პლათფორმა რომელშიც დეველოპერები აზიარებენ თავის ნამუშევრებს. შეიძლება ითქვას რომ  Github-ი 
არის დეველოპერების სოციალური ქსელი. Github-ი არის ყველა დეველოპერების პორთფოლიო.
Git & Github ერთად მუშაობენ

                                        Git-ის ბრძანებები

როცა ახალ პროექტში გვინდა დავაყენოთ Git-ის ვერსიების განახლების ფოლდერი უნდა გამოვიყენოთ git init ბრძანება(ინიციალიზება). git init ბრძანება გამოიყენება მხოლოდ ერთხელ

თუ ახალი ვერსიის შექმნა მინდა პირველ რიგში უნდა ავირჩიო ის ფაილები რომლის განახლება და მოთავსება ახალ ვესიაში
ამისთვის უნდა გამოვიყენოთ git add . ბრძანება.

მე რომ ახალი ვერსია შევქმნა უნდა დავწერო git commit -m "ახალი ვერსიის სახელი" ბრძანება. git commit ბრძანება ქმნის ახალ ვერსიას ხოლო
 -m მაძლებს საშუალებას ახალ ვერსიას მივანიჭო სახელი.

                                       Github-ზე ატვირთვა ტერმინალიდან

 როცა გვინდა ჩვენი პროექტი ავტვირთოთ Github-ზე უნდა შევქმნათ რეპოზიტორია და რაპოზიტორიის შექმნის მერე ამოგვიგდებს
 ბრძანებებს და ჩვენ უნდა გამოვიყენოთ მხოლოდ ბოლო სამი ბრძანება.

                                   Git-ის სხვა ბრძანებები

git branch-ის დახმარებით ვამოწმებთ რამდენი ფოლდერი გვაქ

git branch -M ამ ბრძანებით შეგვიძლია ფოლდერს გადავარქვათ სახელი მაგალითად რომ დავწეროთ git branch -M main  მთავარი master ფოლდერის მაგივრად გვექნება main ფოლდერი

git branch და რომ მივუწეროთ მაგალითად test ჩვენ შევნით ახალ ფაილს სახალად test მაგრამ მაინც გვექნება ერთი მთავარი ფოლდერი სახელად master (ან მთავარი ფოლდერი მაგრამ სხვა სახელით)

git log ბრძანება რომელიც გვეხმარება რომ ვნახოთ რამდენი განახლება გვაქ უკვე ჩვენ ფოლდერში

git checkout ბრძანება რომელიც გვეხმარება გადავიდეთ სხვადასხვა ფოლდერებში (თუ გვაქ ორი ან მეტი ფოლდერი შექმნილი)