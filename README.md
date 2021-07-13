
# ranDOmn-iexec

iExec decentralized oracle for aggregating two random number generator APIs and providing up to 256 random uint numbers.


### Data sources

[ANU QNRG](https://qrng.anu.edu.au/):  Random numbers generated in real-time by measuring the quantum fluctuations of the vacuum.

[CSNRG](csrng.net): [NIST](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/3016) Certified random number generator.

*Note: services provided by these sources do not require a dedicated API key.*

### Aggregation algorithm


    get 256 QNRG random uint8 numbers rqnrg
    get 1 CSNRG random uint8 number rcsnrg
    for n requested numbers :
	    add rqnrg at index rcsnrg to output list
	    set index at next position
	return output list


### IO

input :
- The requested count of uint8 random numbers - a number between 1 and 256 (default is 1).

*example: 5*

output :
- A file containing the list of n random uint8 numbers.
- A file containing the proof of contribution by iExec workers.

*example: [89, 98, 78, 0, 199]*

## Running locally

Build the docker image :

    docker image build -t randomn-iexec .

Run the docker image, only the output folder path is needed

    docker run --rm -it -v $(pwd):/iexec_out -e IEXEC_OUT=/iexec_out randomn-iexec 123

 ## Deploying and running on iExec
