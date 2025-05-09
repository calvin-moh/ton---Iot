import numpy as np
import warnings
from flask import Flask, request, render_template, send_file
import joblib
warnings.filterwarnings("ignore")
app=Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/download/<filename>")
def download_file(filename):
    directory ='files'
    return send_file(f'{directory}/{filename}',as_attachment=True)

@app.route('/predict',methods=['POST'])
def predict():
    form_values_list=list(request.form.values())
    if form_values_list:
        model_name=form_values_list[0]
        model = joblib.load('./static/'+model_name)
    int_features = [float(x) for x in form_values_list[1:]]
    if int_features[0]==0:
        f_features=[0,0,0]+int_features[1:]
    elif int_features[0]==1:
        f_features=[1,0,0]+int_features[1:]
    elif int_features[0]==2:
        f_features=[0,1,0]+int_features[1:]
    else:
        f_features=[0,0,1]+int_features[1:]

    if f_features[6]==0:
        fn_features=f_features[:6]+[0,0]+f_features[7:]
    elif f_features[6]==1:
        fn_features=f_features[:6]+[1,0]+f_features[7:]
    else:
        fn_features=f_features[:6]+[0,1]+f_features[7:]
    final_features = [np.array(fn_features)]
    predict = model.predict(final_features)
    if predict==0:
        output='Normal'
    elif predict==1:
        output='DOS'
    elif predict==2:
        output='PROBE'
    elif predict==3:
        output='R2L'
    else:
        output='U2R'
    return render_template('index.html', output=output, form_values_list=form_values_list)


app.static_folder = 'static'
if __name__ == '__main__':
    app.run()