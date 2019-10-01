FROM python:3.7
RUN mkdir -p /app
COPY SimpleCalc.py /app
WORKDIR /app
ARG OPE_RATION
ARG NUM_BER
#RUN python SimpleCalc.py 
#ENTRYPOINT ["SimpleCalc.py"]
CMD ["python /app/SimpleCalc.py", "OPE_RATION", "NUM_BER"]
